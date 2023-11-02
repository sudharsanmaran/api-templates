from src.schemas import BaseFieldValidations
from pydantic import Field

class SendTweet(BaseFieldValidations):
    text: str = Field(...,description="The text required for tweet")