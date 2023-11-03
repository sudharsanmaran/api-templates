from pydantic import BaseModel
from typing import Optional, List


class EmailAddress(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None


class Recipient(BaseModel):
    emailAddress: EmailAddress = None


class ItemBody(BaseModel):
    contentType: Optional[str] = None
    content: Optional[str] = None
