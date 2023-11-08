from pydantic import ValidationError

from src.constants import AllActions, Status
from src.microsoft.client import MSGraphClient
from src.microsoft.validations import validate_send_mail, validate_busy_or_free_schedule
from src.utils import get_request_body, get_action_form

client = MSGraphClient()


def handle_error(errors, all_fields, prompt, action_name):
    # TODO: handle errors
    return get_action_form(
        Status.error,
        action_name,
        prompt,
        all_fields,
    )


def send_email(data: dict):
    global client
    prompt = data["data"]["prompt"]
    action_name = data["data"]["action_name"]
    fields = data["data"]["fields"]
    request_body = get_request_body(data)
    try:
        valid_request_body = validate_send_mail(request_body)
    except ValidationError as e:
        print('Error came!')
        return handle_error(e.errors(), fields, prompt, action_name)

    if not data["data"]["validate_only"]:
        try:
            result = client.send_email(**valid_request_body.model_dump())
        except Exception as err:
            return handle_error(err, fields, prompt, action_name)

    result = get_action_form(
        Status.success,
        AllActions.microsoft_send_email,
        prompt,
        fields,
    )
    return result


def microsoft_retrieve_free_or_busy_schedule(data: dict):
    global client
    prompt = data["data"]["prompt"]
    action_name = data["data"]["action_name"]
    fields = data["data"]["fields"]
    request_body = get_request_body(data)
    try:
        valid_request_body = validate_busy_or_free_schedule(request_body)
    except ValidationError as e:
        print('Error came!')
        return handle_error(e.errors(), fields, prompt, action_name)

    if not data["data"]["validate_only"]:
        try:
            result = client.get_free_or_busy_schedule(**valid_request_body.model_dump())
        except Exception as err:
            return handle_error(err, fields, prompt, action_name)

    result = get_action_form(
        Status.success,
        AllActions.microsoft_retrieve_free_or_busy_schedule,
        prompt,
        fields,
    )
    return result


actions = {
    AllActions.microsoft_send_email: send_email,
    AllActions.microsoft_retrieve_free_or_busy_schedule: microsoft_retrieve_free_or_busy_schedule
}
