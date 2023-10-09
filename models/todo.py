from sqlmodel import Field

from models.base import BaseUUIDModel


class Todo(BaseUUIDModel, table=True):
    content: str = Field(default="!")
    done: bool = Field(default=False)
    description: str | None = Field(default=None)

    __tablename__ = "todo"
