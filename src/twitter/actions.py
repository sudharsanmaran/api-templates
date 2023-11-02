from .client import Client
from src.utils import get_request_body

client = Client()

def send_tweet(data: dict):
    global client
    body = get_request_body(data)
    result = client.send_tweet(**body)
    # TODO convert result to ActionForms format
    return result




