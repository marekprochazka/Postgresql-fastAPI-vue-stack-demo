from typing import TypedDict

from repositories.base import M

def model_to_api(instance: M) -> dict:
    return instance.to_dict()


def list_to_api(instances: list[M]) -> list[dict]:
    return [model_to_api(instance) for instance in instances]


def selected_fields(instance: M, fields: list[str]) -> dict:
    for field in fields:
        if not hasattr(instance, field):
            raise AttributeError(f"{field} is not a valid attribute")
    return {field: getattr(instance, field) for field in fields}


def selected_fields_list(instances: list[M], fields: list[str]) -> list[dict]:
    return [selected_fields(instance, fields) for instance in instances]


