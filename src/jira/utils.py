from datetime import datetime, timedelta


def str2dict(scopes: str) -> dict:
    return {s: True for s in scopes.split()}


def dict2str(scopes: dict) -> str:
    return " ".join(k for k in scopes.keys())


def seconds2currentTime(expires_in_seconds: int) -> datetime:
    return (
        datetime.now()
        + timedelta(seconds=expires_in_seconds)
        - timedelta(minutes=1)
    )


def get_new_resource_from(old_res, new_res):
    if old_res:
        ids = [str(obj.resource_id) for obj in old_res]
        return [d["id"] for d in new_res if d["id"] not in ids]
    return new_res[0]
