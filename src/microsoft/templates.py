from src.constants import AllActions
from src.schemas import Template, FieldTemplate

from .constants import SCOPES

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
        value=SCOPES[AllActions.microsoft_send_email],
        label="Scope",
        type_of="input",
        scenario=scenario,
    )
    access_token = create_field_template(
        field_name="access_token",
        label="Access Token",
        type_of="input",
        required=True,
        scenario="google_credentials",
    )
    to = create_field_template(
        field_name="to",
        label="To",
        type_of="input",
        required=True,
        scenario=scenario,
        priority=2,
    )
    subject = create_field_template(
        field_name="subject",
        label="Subject",
        type_of="input",
        required=True,
        scenario=scenario,
        priority=2,
    )
    body = create_field_template(
        field_name="body",
        label="Body",
        type_of="input",
        required=True,
        scenario=scenario,
        priority=2,
    )
    cc = create_field_template(
        field_name="cc",
        label="CC",
        type_of="input",
        scenario=scenario,
        priority=2,
    )
    bcc = create_field_template(
        field_name="bcc",
        label="BCC",
        type_of="input",
        scenario=scenario,
        priority=2,
    )
    id = 1
    fields = [scope, access_token, to, subject, body, cc, bcc]

    template = Template(
        id=id,
        provider=provider,
        action_name=AllActions.google_send_email,
        fields=fields,
    )
    return template


templates = {AllActions.microsoft_send_email: send_email}
