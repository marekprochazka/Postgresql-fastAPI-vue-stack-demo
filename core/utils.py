from repositories.base import M


def model_to_api(instance: M) -> dict:
    return instance.to_dict()


def list_to_api(instances: list[M]) -> list[dict]:
    return [model_to_api(instance) for instance in instances]
