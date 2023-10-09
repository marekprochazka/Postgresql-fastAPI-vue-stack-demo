from datetime import datetime
from typing import TypeVar, Generic
from uuid import UUID

from pydantic import BaseModel
from sqlmodel import Session
from sqlmodel import select

import abc


from models.base import BaseUUIDModel

M = TypeVar("M", bound=BaseUUIDModel)
R = TypeVar("R", bound=BaseModel)
L = TypeVar("L", bound=BaseModel)
C = TypeVar("C", bound=BaseModel)
P = TypeVar("P", bound=BaseModel)


class DoesNotExist(Exception):
    pass


"""
TODO add filter params to list method?
"""


class BaseModelRepository(abc.ABC, Generic[M, R, L, C, P]):
    model: type[M] = None
    session: Session = None
    schema_retrieve: type[R] = None
    schema_list: type[R] = None
    schema_create: type[C] = None
    schema_patch: type[P] = None

    def __init__(self, session: Session):
        self.session = session

        if not issubclass(self.model, BaseUUIDModel):
            raise NotImplementedError(
                "model must be subclass of models.base.BaseUUIDModel"
            )

        if not issubclass(self.schema_retrieve, BaseModel):
            raise NotImplementedError(
                "schema_retrieve must be subclass of pydantic.BaseModel"
            )

        if not issubclass(self.schema_list, BaseModel):
            raise NotImplementedError(
                "schema_list must be subclass of pydantic.BaseModel"
            )

    def __get_instance(self, instance_id: UUID) -> M:
        statement = (
            select(self.model)
            .where(self.model.id == instance_id)
        )
        instance = self.session.exec(statement).first()
        if instance is None:
            raise DoesNotExist
        return instance

    def get(self, instance_id: UUID) -> R:
        return self.schema_retrieve.from_orm(self.__get_instance(instance_id))

    def create(self, schema_instance: C) -> R:
        instance = self.model(**schema_instance.dict())
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def get_list_statement(self) -> select:
        return select(self.model)

    def list(self, limit: int | None = None) -> list[L]:
        statement = self.get_list_statement()
        if limit is not None:
            statement = statement.limit(limit)
        return [self.schema_list.from_orm(instance) for instance in self.session.exec(statement)]

    def patch(self, instance_id: UUID, patch_data: P) -> R:
        instance = self.__get_instance(instance_id)
        instance.x_updated = datetime.utcnow()
        for field, value in patch_data.dict(exclude_unset=True).items():
            setattr(instance, field, value)
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return self.schema_retrieve.from_orm(instance)

    def delete(self, instance_id: UUID) -> None:
        instance = self.__get_instance(instance_id)
        self.session.delete(instance)
        self.session.commit()
