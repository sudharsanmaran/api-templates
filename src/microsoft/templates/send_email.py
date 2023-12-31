from src.constants import AllActions
from src.microsoft.constants import SCOPES, REGEX
from src.schemas import Template
from .base import create_field_template

provider = 'microsoft'


def send_email():
    scenario = 'Mail.Send'
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
        scenario='',
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
