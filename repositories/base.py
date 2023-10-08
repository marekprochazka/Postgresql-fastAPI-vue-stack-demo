from typing import TypeVar, Generic
from uuid import UUID

from sqlmodel import Session, SQLModel
from sqlmodel import select

import abc

M = TypeVar("M", bound=SQLModel)


class DoesNotExist(Exception):
    pass


"""
TODO add filter params to list method?
"""


class BaseModelRepository(abc.ABC, Generic[M]):
    model: M = None
    session: Session = None

    def __init__(self, session: Session):
        self.session = session

        if not issubclass(self.model, SQLModel):
            raise NotImplementedError(
                "model must be subclass of sqlmodel.SQLModel"
            )

    def get_instance(self, instance_id: UUID) -> M:
        statement = (
            select(self.model)
            .where(self.model.id == instance_id)
        )
        instance = self.session.exec(statement).first()
        if instance is None:
            raise DoesNotExist
        return instance

    def create(self, instance: M) -> M:
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def list(self, limit: int | None = None) -> list[M]:
        statement = select(self.model)
        if limit is not None:
            statement = statement.limit(limit)
        return self.session.exec(statement).all()

    def patch(self, instance_id, patch_data: dict) -> M:
        instance = self.get_instance(instance_id)
        for key, value in patch_data.items():
            if not hasattr(instance, key):
                raise AttributeError(f"{key} is not a valid attribute")
            setattr(instance, key, value)
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def delete(self, instance_id: UUID) -> None:
        instance = self.get_instance(instance_id)
        self.session.delete(instance)
        self.session.commit()
