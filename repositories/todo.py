from models.todo import Todo
from repositories.base import BaseModelRepository


class TodoRepository(BaseModelRepository[Todo]):
    model = Todo
    pass
