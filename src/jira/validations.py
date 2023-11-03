from pydantic import ValidationError
from .schemas import CreateProjectRequest
import logging

logger = logging.getLogger(__name__)


def validate_create_project(data: CreateProjectRequest):
    try:
        request_body = CreateProjectRequest(**data)
    except ValidationError as e:
        logger.error(e.errors())
        raise e
    return request_body
