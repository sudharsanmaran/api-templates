from src.constants import AllActions
from src.schemas import Template, FieldTemplate

from constants import SCOPES

provider = "microsoft"


def create_field_template(
        field_name, label, scenario, value='',
        type_of='input', required=False, default='',
        options=None, validator='', priority=1,
        save_to_history=False
):
    if options is None:
        options = []
    return FieldTemplate(
        field_name=field_name,
        value=value,
        label=label,
        type=type_of,
        required=required,
        default=default,
        options=options,
        validator=validator,
        scenario=scenario,
        priority=priority,
        save_to_history=save_to_history,
    )


def send_email():
    # id = 1
    scenario = "google_email_send"
    scope = create_field_template(
        field_name="scope",
        value=SCOPES[AllActions.google_send_email],
        label="Scope",
        type_of="input",
        scenario=scenario,
    )
    access_token = FieldTemplate(
        field_name="access_token",
        label="Access Token",
        type="input",
        required=True,
        scenario="google_credentials",
    )
    to = FieldTemplate(
        field_name="to",
        label="To",
        type="input",
        required=True,
        scenario=scenario,
        priority=2,
    )
    subject = FieldTemplate(
        field_name="subject",
        label="Subject",
        type="input",
        required=True,
        scenario=scenario,
        priority=2,
    )
    body = FieldTemplate(
        field_name="body",
        label="Body",
        type="input",
        required=True,
        scenario=scenario,
        priority=2,
    )
    cc = FieldTemplate(
        field_name="cc",
        label="CC",
        type="input",
        scenario=scenario,
        priority=2,
    )
    bcc = FieldTemplate(
        field_name="bcc",
        label="BCC",
        type="input",
        scenario=scenario,
        priority=2,
    )
    template = Template(
        # id=id,
        provider=provider,
        action_name=AllActions.google_send_email,
        fields=[scope, access_token, to, subject, body, cc, bcc],
    )
    return template


templates = {AllActions.microsoft_send_email: send_email}
