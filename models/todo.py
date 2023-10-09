from sqlmodel import BigInteger, Column, Field, SQLModel

from models.base import BaseUUIDModel


class Todo(BaseUUIDModel, table=True):
    content: str = Field(default="!")
    done: bool = Field(default=False)

    __tablename__ = "todo"
