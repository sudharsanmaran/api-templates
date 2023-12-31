import re
from pydantic import Field, validator
from .constants import REGEX, regex_patterns
from src.schemas import BaseFieldValidations


class SendMail(BaseFieldValidations):
    to: str = Field(
        ...,
        description="The email address of the recipients",
    )
    from_email: str = Field(
        ...,
        description="The email address of the sender",
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

    @validator("cc", "bcc")
    def check_emails(cls, v):
        regex = REGEX.EMPTY_OR_SINGLE_OR_MULTIPLE_EMAILS
        if not re.match(regex, v):
            raise ValueError("Invalid email address")
        return [email.strip() for email in v.split(",")]

    @validator("to")
    def check_to_email(cls, v):
        regex = REGEX.SINGLE_OR_MULTIPLE_EMAILS
        if not re.match(regex, v):
            raise ValueError("Invalid email address")
        return [email.strip() for email in v.split(",")]

    @validator("from_email")
    def check_from_email(cls, v):
        regex = REGEX.SINGLE_EMAIL
        if not re.match(regex, v):
            raise ValueError("Invalid email address")
        return v


class CalendarEvent(BaseFieldValidations):
    summary: str = Field("", description="The summary of the event")
    description: str = Field("", description="The description of the event")
    start: str = Field(..., description="The start date and time of the event")
    end: str = Field(..., description="The end date and time of the event")
    timezone: str = Field(..., description="The timezone of the event")
    attendees: str = Field(
        "",
        description="The email address of the attendees",
    )
    location: str = Field(
        "",
        description="The location of the event",
    )
    # recurrence: str = Field(
    #     "",
    #     description="The recurrence of the event",
    # )
    # reminders: str = Field(
    #     "",
    #     description="The reminders of the event",
    # )

    @validator("attendees")
    def check_emails(cls, v):
        regex = REGEX.EMPTY_OR_SINGLE_OR_MULTIPLE_EMAILS
        if not re.match(regex, v):
            raise ValueError("Invalid email address")
        return [email.strip() for email in v.split(",")]

    @validator("start", "end")
    def check_date(cls, v):
        pattern = regex_patterns["DATETIME"]
        if not re.match(pattern, v):
            raise ValueError("Invalid date")
        return v

    # @validator("recurrence")
    # def check_recurrence(cls, v):
    #     return v.split(",")
