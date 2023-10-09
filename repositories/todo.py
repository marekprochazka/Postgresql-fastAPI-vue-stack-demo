from models.todo import Todo
from repositories.base import BaseModelRepository
from schemas.todo import TodoRetrieve, TodoList, TodoCreate, TodoPatch


class TodoRepository(BaseModelRepository[Todo, TodoRetrieve, TodoList, TodoCreate, TodoPatch]):
    model = Todo
    schema_retrieve = TodoRetrieve
    schema_list = TodoList
    schema_create = TodoCreate
    schema_patch = TodoPatch
