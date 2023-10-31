from src.constants import AllActions
from .client import Client
from src.utils import get_request_body


client = Client()


def send_email(data: dict):
    global client
    body = get_request_body(data)
    result = client.send_email(**body)
    # TODO convert result to ActionForms format
    return result


def create_calendar_event(data: dict):
    global client
    body = get_request_body(data)
    result = client.create_calendar_event(**body)
    # TODO convert result to ActionForms format
    return result


actions = {
    AllActions.google_send_email: send_email,
    AllActions.google_create_calendar_event: create_calendar_event,
}
