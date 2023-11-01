from pydantic import ValidationError
from .schemas import CalendarEvent, SendMail
import logging

logger = logging.getLogger(__name__)


def validate_send_mail(data: SendMail):
    try:
        request_body = SendMail(**data)
    except ValidationError as e:
        logger.error(e.errors())
        raise e
    return request_body


def validate_calendar_event(data: dict):
    try:
        request_body = CalendarEvent(**data)
    except ValidationError as e:
        logger.error(e.errors())
        raise e
    return request_body
