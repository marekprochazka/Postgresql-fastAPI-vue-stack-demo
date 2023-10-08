from fastapi import APIRouter, HTTPException

from db import get_session, generate_engine
from repositories.todo import TodoRepository

router = APIRouter(tags=["todos"])


@router.get("/list")
async def todos() -> dict:
    session = get_session(generate_engine())
    repository = TodoRepository(session)
    return {"status": "ok", "todos": repository.list()}
