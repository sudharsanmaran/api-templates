from pydantic import ValidationError
from src.utils import get_action_form, get_request_body
from .client import Client
from src.constants import Status, AllActions
from .validations import validate_send_tweet

client = Client()


def handle_error(errors, all_fields, prompt, action_name):
    # TODO: handle errors
    return get_action_form(
        Status.error,
        action_name,
        prompt,
        all_fields,
    )


def send_tweet(data: dict):
    global client
    prompt = data["data"]["prompt"]
    action_name = data["data"]["action_name"]
    fields = data["data"]["fields"]
    request_body = get_request_body(data)
    try:
        valid_request_body = validate_send_tweet(request_body)
    except ValidationError as e:
        return handle_error(e.errors(), fields, prompt, action_name)

    if not data["data"]["validate_only"]:
        try:
            result = client.send_tweet(**valid_request_body.model_dump())
        except Exception as err:
            return handle_error(err, fields, prompt, action_name)

    result = get_action_form(
        Status.success,
        action_name,
        prompt,
        fields,
    )
    return result


actions = {AllActions.twitter_write_tweet: send_tweet}
