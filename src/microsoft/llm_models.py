from pydantic import BaseModel, Field


class Email(BaseModel):
    subject: str = Field(
        ..., title="Main subject of the mail, generate from the prompt\
            and avoid using email ids or name in the subject"
    )
    body_content: str = Field(
        ...,
        title="Body of the mail, generate from the subject and avoid \
            using email ids or name in the body",
    )