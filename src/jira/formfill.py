from src.jira.utils import conbine_name_id
from src.constants import AllActions, Status
from src.utils import get_action_form
from .client import Client

client = Client()


def handle_error(errors, all_fields, prompt, action_name):
    return get_action_form(
        Status.error,
        action_name,
        prompt,
        all_fields,
    )


async def create_project(data: dict):
    try:
        fields = data["data"]["fields"]
        prompt = data["data"]["prompt"]
        action_name = data["data"]["action_name"]
        access_token = next(
            (item["value"] for item in fields if item["field_name"] == "access_token"),
            None,
        )

        if not access_token:
            raise ValueError("Access token not found in data")

        resource_id_field = next(
            (item for item in fields if item["field_name"] == "resource_id"), None
        )

        lead_id_field = next(
            (item for item in fields if item["field_name"] == "leadAccountId"), None
        )

        resource_response = await client.get_user_accessible_resources(access_token)
        user_response = await client.get_Jira_user(access_token)

        resource_id_field["options"] = [
            conbine_name_id(res["name"], res["id"]) for res in resource_response
        ]

        lead_id_field["value"] = user_response['account_id']

    except Exception as err:
        return handle_error(err, fields, prompt, action_name)
    return get_action_form(
        Status.success,
        action_name,
        prompt,
        fields,
    )


formfills = {AllActions.jira_create_project: create_project}
