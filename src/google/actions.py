from pydantic import ValidationError

from src.constants import AllActions, Status
from src.utils import get_action_form, get_request_body
from .client import Client

# from .templates import fields as google_fields
from .validations import validate_send_mail, validate_calendar_event

client = Client()


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
        return handle_error(e.errors(), fields, prompt, action_name)

    if not data["data"]["validate_only"]:
        try:
            result = client.send_email(**valid_request_body.model_dump())
        except Exception as err:
            return handle_error(err, fields, prompt, action_name)

    result = get_action_form(
        Status.success,
        AllActions.google_send_email,
        prompt,
        fields,
    )
    return result


def create_calendar_event(data: dict):
    global client
    prompt = data["data"]["prompt"]
    action_name = data["data"]["action_name"]
    fields = data["data"]["fields"]
    request_body = get_request_body(data)
    try:
        valid_request_body = validate_calendar_event(request_body)
    except ValidationError as e:
        return handle_error(e.errors(), fields, prompt, action_name)

    if not data["data"]["validate_only"]:
        try:
            result = client.create_calendar_event(**valid_request_body)
        except Exception as err:
            return handle_error(err, fields, prompt, action_name)

    result = get_action_form(
        Status.success,
        AllActions.google_create_calendar_event,
        prompt,
        fields,
    )
    return result


actions = {
    AllActions.google_send_email: send_email,
    AllActions.google_create_calendar_event: create_calendar_event,
}
