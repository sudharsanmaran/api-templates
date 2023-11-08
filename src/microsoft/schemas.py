from src.schemas import BaseFieldValidations
from pydantic import Field
from typing import Optional


class SendEmail(BaseFieldValidations):
    toRecipients: str = Field(
        ...,
        description='The email address of the recipients',
    )
    from_email: Optional[str] = Field(
        None,
        description='The email address of the sender',
    )
    subject: str = Field(..., description='The subject of the email')
    body_content_type: Optional[str] = Field(..., description='The body type of email, it can be text or html')
    body_content: str = Field(..., description='The body of the email')
    ccRecipients: Optional[str] = Field(
        None,
        description='The email address of the CC recipients',
    )
    bccRecipients: Optional[str] = Field(
        None,
        description='The email address of the BCC recipients',
    )

    saveToSentItems: Optional[str] = Field(
        None,
        description='Indicates whether to save the message in Sent Items.'
    )


class GetFreeOrBusySchedule(BaseFieldValidations):
    schedules: Optional[str] = Field(
        description='Email of particular person.'
    )
    start_time: Optional[str] = Field(
        description='Start time.'
    )
    end_time: Optional[str] = Field(
        description='End time.'
    )
    timezone: Optional[str] = Field(
        description='Timezone'
    )
