from datetime import datetime
from uuid import UUID

from schemas.base import BaseSchema


class TodoRetrieve(BaseSchema):
    id: UUID
    content: str
    done: bool
    x_created: datetime


class TodoList(TodoRetrieve):
    pass


class TodoCreate(BaseSchema):
    content: str
    done: bool = False


class TodoPatch(BaseSchema):
    content: str | None
    done: bool | None
