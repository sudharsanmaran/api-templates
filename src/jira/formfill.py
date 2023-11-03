from src.constants import AllActions
from .client import Client

client = Client()


async def create_project(data: dict):
    data_temp = data["data"]["fields"]
    access_token = next(
        (item["value"] for item in data_temp if item["field_name"] == "access_token"),
        None,
    )

    if not access_token:
        raise ValueError("Access token not found in data")

    resource_id_field = next(
        (item for item in data_temp if item["field_name"] == "resource_id"), None
    )

    if not resource_id_field:
        raise ValueError("Resource ID field not found in data")

    response = await client.get_user_accessible_resources(access_token)

    resource_id_field["options"] = [res["id"] for res in response]

    return data


# formfills = {AllActions.jira_create_project: create_project}
