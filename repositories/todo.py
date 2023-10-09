from models.todo import Todo
from repositories.base import BaseModelRepository
from schemas.todo import TodoRetrieve, TodoList, TodoCreate, TodoPatch


class TodoRepository(BaseModelRepository[Todo, TodoRetrieve, TodoList, TodoCreate, TodoPatch]):
    model = Todo
    schema_retrieve = TodoRetrieve
    schema_list = TodoList
    schema_create = TodoCreate
    schema_patch = TodoPatch

    def filter_by_done_statement(self, done: bool):
        return self.get_base_list_statement().where(self.model.done == done)

    def list_by_done(self, limit: int | None = None, done: bool = False) -> list[TodoList]:
        return self.list(limit, self.filter_by_done_statement(done))
