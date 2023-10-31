from src.constants import AllActions
from src.schemas import Template, FieldTemplate

from .constants import SCOPES


provider = "google"


def send_email():
    id = 1
    scenario = "google_email_send"
    scope = FieldTemplate(
        field_name="scope",
        value=SCOPES[AllActions.google_send_email],
        label="Scope",
        type="input",
        required=False,
        default="",
        options=[],
        validator="",
        scenario=scenario,
        priority=1,
        save_to_history=False,
    )
    access_token = FieldTemplate(
        field_name="access_token",
        value="",
        label="Access Token",
        type="input",
        required=True,
        default="",
        options=[],
        validator="",
        scenario="google_credentials",
        priority=1,
        save_to_history=False,
    )
    to = FieldTemplate(
        field_name="to",
        value="",
        label="To",
        type="input",
        required=True,
        default="",
        options=[],
        validator="",
        scenario=scenario,
        priority=2,
        save_to_history=False,
    )
    subject = FieldTemplate(
        field_name="subject",
        value="",
        label="Subject",
        type="input",
        required=True,
        default="",
        options=[],
        validator="",
        scenario=scenario,
        priority=2,
        save_to_history=False,
    )
    body = FieldTemplate(
        field_name="body",
        value="",
        label="Body",
        type="input",
        required=True,
        default="",
        options=[],
        validator="",
        scenario=scenario,
        priority=2,
        save_to_history=False,
    )
    cc = FieldTemplate(
        field_name="cc",
        value="",
        label="CC",
        type="input",
        required=False,
        default="",
        options=[],
        validator="",
        scenario=scenario,
        priority=2,
        save_to_history=False,
    )
    bcc = FieldTemplate(
        field_name="bcc",
        value="",
        label="BCC",
        type="input",
        required=False,
        default="",
        options=[],
        validator="",
        scenario=scenario,
        priority=2,
        save_to_history=False,
    )
    template = Template(
        id=id,
        provider=provider,
        action_name=AllActions.google_send_email,
        fields=[scope, access_token, to, subject, body, cc, bcc],
    )
    return template


def calendar_event():
    pass


templates = {AllActions.google_send_email: send_email}
