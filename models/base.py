from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel
import abc


class BaseUUIDModel(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    x_created: datetime = Field(default_factory=datetime.utcnow)
    x_updated: datetime = Field(default_factory=datetime.utcnow, index=True)

    def __init__(self, **kwargs):
        if not self.__tablename__:
            raise NotImplementedError(
                f"__tablename__ not defined in {self.__class__.__name__}"
            )
        super().__init__(**kwargs)
