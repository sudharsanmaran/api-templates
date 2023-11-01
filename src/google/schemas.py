import re
from pydantic import Field, validator
from .constants import REGEX
from src.schemas import BaseFieldValidations


class SendMail(BaseFieldValidations):
    to: str = Field(
        ...,
        description="The email address of the recipients",
    )
    subject: str = Field(..., description="The subject of the email")
    body: str = Field(..., description="The body of the email")
    cc: str = Field(
        ...,
        description="The email address of the CC recipients",
    )
    bcc: str = Field(
        ...,
        description="The email address of the BCC recipients",
    )

    @validator("to", "cc", "bcc")
    def check_emails(cls, v):
        regex = REGEX.LIST_OF_EMAILS
        if not re.match(regex, v):
            raise ValueError("Invalid email address")
        return v
