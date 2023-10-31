from src.constants import AllActions
from client import MSGraphClient
from src.utils import get_request_body

client = MSGraphClient()


def send_email(data: dict):
    global client
    body = get_request_body(data)
    result = client.send_email(**body)
    # TODO convert result to ActionForms format
    return result


actions = {
    AllActions.microsoft_send_email: send_email,
}
