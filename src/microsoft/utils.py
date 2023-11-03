from src.microsoft.sub_schemas import Recipient, EmailAddress, ItemBody


def generateEmailRecipient(email: str):
    email_address = EmailAddress()
    email_address.address = email
    recipient = Recipient()
    recipient.email_address = email_address

    return recipient


def generateBody(body_content_type, body_content):
    item_body = ItemBody()
    item_body.content = body_content
    item_body.contentType = body_content_type
    return item_body


