from pydantic import ValidationError
from .client import Client
from .validations import validate_create_project
from src.constants import AllActions, Status
from src.utils import get_action_form, get_request_body

client = Client()


def handle_error(errors, all_fields, prompt, action_name):
    return get_action_form(
        Status.error,
        action_name,
        prompt,
        all_fields,
    )


async def create_project(data: dict):
    global client
    prompt = data["data"]["prompt"]
    action_name = data["data"]["action_name"]
    fields = data["data"]["fields"]
    request_body = get_request_body(data)
    try:
        valid_request_body = validate_create_project(request_body)
    except ValidationError as e:
        return handle_error(e.errors(), fields, prompt, action_name)

    if not data["data"]["validate_only"]:
        try:
            result = await client.create_project(**valid_request_body.model_dump())
        except Exception as err:
            return handle_error(err, fields, prompt, action_name)

    result = get_action_form(
        Status.success,
        AllActions.jira_create_project,
        prompt,
        fields,
    )
    return result


actions = {
    AllActions.jira_create_project: create_project,
}
