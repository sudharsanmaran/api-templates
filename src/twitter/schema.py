from src.schemas import BaseFieldValidations
from pydantic import Field, validator


class SendTweet(BaseFieldValidations):
    text: str = Field(..., description="The text required for tweet")

    @validator('text')
    def check_empty_string(cls, v):
        if v == "":
            raise ValueError("Text field should not be an empty string.")
        return v

