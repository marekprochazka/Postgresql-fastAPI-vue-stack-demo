from fastapi import APIRouter, HTTPException

from db import get_session, generate_engine
from repositories.todo import TodoRepository

router = APIRouter(tags=["todos"])


# TODO docs don't work on this (some serialization needed)
@router.get("/list")
async def todos() -> dict:
    session = get_session(generate_engine())
    repository = TodoRepository(session)
    return {"status": "ok", "todos": repository.list()}
