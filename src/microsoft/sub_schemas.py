from pydantic import BaseModel
from typing import Optional


class EmailAddress(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None


class Recipient(BaseModel):
    email_address: Optional[EmailAddress] = None


class ItemBody(BaseModel):
    contentType: Optional[str] = None
    content: Optional[str] = None
