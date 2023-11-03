from src.constants import AllActions
from src.schemas import Template, FieldTemplate

from .constants import SCOPES, REGEX

provider = 'microsoft'


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
    scenario = 'google_email_send'
    scope = create_field_template(
        field_name='scope',
        value=SCOPES[AllActions.microsoft_send_email],
        label='Scope',
        type_of='input',
        scenario=scenario,
    )
    access_token = create_field_template(
        field_name='access_token',
        label='Access Token',
        type_of='input',
        required=True,
        scenario='google_credentials',
    )
    toRecipients = create_field_template(
        field_name='toRecipients',
        label='To Recipients',
        type_of='input',
        required=True,
        scenario=scenario,
        priority=2,
        validator=REGEX.SINGLE_OR_MULTIPLE_EMAILS.value
    )
    from_email = create_field_template(
        field_name='from_email',
        label='From Email',
        type_of='input',
        required=False,
        scenario=scenario,
        priority=2,
        validator=REGEX.SINGLE_OR_MULTIPLE_EMAILS.value
    )
    subject = create_field_template(
        field_name='subject',
        label='Subject',
        type_of='input',
        required=True,
        scenario=scenario,
        priority=2,
    )

    body_content_type = create_field_template(
        field_name='body_content_type',
        label='Body Content Type',
        type_of='checkbox',
        required=True,
        scenario=scenario,
        default='Text',
        priority=2,
        options=['Text', 'Html']
    )

    body_content = create_field_template(
        field_name='body_content',
        label='Body Content',
        type_of='input',
        required=True,
        scenario=scenario,
        priority=2,
    )

    ccRecipients = create_field_template(
        field_name='ccRecipients',
        label='CC Recipients',
        type_of='input',
        scenario=scenario,
        priority=2,
        validator=REGEX.SINGLE_OR_MULTIPLE_EMAILS.value
    )
    bccRecipients = create_field_template(
        field_name='bccRecipients',
        label='BCC Recipients',
        type_of='input',
        scenario=scenario,
        priority=2,
        validator=REGEX.SINGLE_OR_MULTIPLE_EMAILS.value
    )

    saveToSentItems = create_field_template(
        field_name='saveToSentItems',
        label='SaveToSentItems',
        type_of='checkbox',
        priority=3,
        scenario=scenario,
        options=['', 'False', 'True'],
        default='True'

    )

    id = 1
    fields = [
        scope, access_token, toRecipients, subject, from_email, body_content,
        body_content_type, ccRecipients, bccRecipients, saveToSentItems
    ]

    template = Template(
        id=id,
        provider=provider,
        action_name=AllActions.microsoft_send_email,
        fields=fields,
    )
    return template


templates = {AllActions.microsoft_send_email: send_email}
