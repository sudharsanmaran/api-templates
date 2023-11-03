import logging

from pydantic import ValidationError

from src.microsoft.schemas import SendEmail
from fastapi.encoders import jsonable_encoder

logger = logging.getLogger(__name__)


def validate_send_mail(data: SendEmail):
    try:
        request_body = SendEmail(**jsonable_encoder(data))
    except ValidationError as e:
        logger.error(e.errors())
        raise e
    return request_body
