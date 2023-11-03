from pydantic import ValidationError
from .schema import SendTweet
import logging

logger = logging.getLogger(__name__)


def validate_send_tweet(data: SendTweet):
    try:
        request_body = SendTweet(**data)
    except ValidationError as e:
        logger.error(e.errors())
        raise e
    return request_body
