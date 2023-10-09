from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Query

from api.utils.dependencies import get_repository
from repositories.todo import TodoRepository

router = APIRouter(tags=["todos"])


@router.get(
    "/list",
    response_model=list[Optional[TodoRepository.schema_list]],
    status_code=200,
    summary="List todos",
    name="todos:list",
)
async def todos(
    limit: int = Query(default=10, ge=1, le=100),
) -> list[Optional[TodoRepository.schema_list]]:
    repository = get_repository(TodoRepository)
    return repository.list(limit)


@router.post(
    "/create",
    response_model=TodoRepository.schema_retrieve,
    status_code=201,
    summary="Create todo",
    name="todos:create",
)
async def create_todo(
    schema: TodoRepository.schema_create,
) -> TodoRepository.schema_retrieve:
    repository = get_repository(TodoRepository)
    return repository.create(schema)


@router.get(
    "/{todo_id}",
    response_model=TodoRepository.schema_retrieve,
    status_code=200,
    summary="Retrieve specific todo",
    name="todos:retrieve",
)
async def retrieve_todo(
    todo_id: UUID,
) -> TodoRepository.schema_retrieve:
    repository = get_repository(TodoRepository)
    return repository.get(todo_id)


@router.patch(
    "/{todo_id}",
    response_model=TodoRepository.schema_retrieve,
    status_code=200,
    summary="Patch specific todo",
    name="todos:patch",
)
async def patch_todo(
    todo_id: UUID,
    schema: TodoRepository.schema_patch,
) -> TodoRepository.schema_retrieve:
    repository = get_repository(TodoRepository)
    return repository.patch(todo_id, schema)


@router.delete(
    "/{todo_id}",
    status_code=204,
    summary="Delete specific todo",
    name="todos:delete",
)
async def delete_todo(
    todo_id: UUID,
) -> None:
    repository = get_repository(TodoRepository)
    repository.delete(todo_id)


@router.get(
    "/list/filter",
    response_model=list[Optional[TodoRepository.schema_list]],
    status_code=200,
    summary="List todos by done query param (default is False)",
    name="todos:list_by_done",
)
async def todos_by_done(
    limit: int = Query(default=10, ge=1, le=100),
    done: bool = Query(default=False),
) -> list[Optional[TodoRepository.schema_list]]:
    repository = get_repository(TodoRepository)
    return repository.list_by_done(limit, done)
