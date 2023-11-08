import datetime

from src.microsoft.sub_schemas import Recipient, EmailAddress, ItemBody, DateTimeFormat


def generateEmailRecipient(email: str):
    email_address = EmailAddress()
    email_address.address = email
    recipient = Recipient()
    recipient.emailAddress = email_address

    return recipient


def generateBody(body_content_type, body_content):
    item_body = ItemBody()
    item_body.content = body_content
    item_body.contentType = body_content_type
    return item_body


def del_none(d):
    """
    Delete keys with the value "None" in a dictionary, recursively.

    This alters the input so you may wish to "copy" the dict first.
    """
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d


def get_date_with_time_zone(timestamp, timezone):
    datetime_format = DateTimeFormat()
    datetime_format.dateTime = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%dT%H:%M:%S')
    datetime_format.timeZone = timezone
    return datetime_format
