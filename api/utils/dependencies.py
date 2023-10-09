from typing import Type, TypeVar

from db import get_session, generate_engine
from repositories.base import BaseModelRepository

R = TypeVar("R", bound=BaseModelRepository)


def get_repository(repository: Type[R]) -> R:
    return repository(get_session(generate_engine()))
