from src.constants import AllActions
from src.schemas import Template, FieldTemplate

from .constants import REGEX, SCOPES


provider = "google"


def to(
    field_name: str = "to",
    value: str = "",
    label="To",
    type="input",
    required=True,
    default="",
    options=[],
    validator=REGEX.LIST_OF_EMAILS,
    scenario="google_email_send",
    priority=2,
    save_to_history=False,
) -> FieldTemplate:
    return FieldTemplate(
        field_name=field_name,
        value=value,
        label=label,
        type=type,
        required=required,
        default=default,
        options=options,
        validator=validator,
        scenario=scenario,
        priority=priority,
        save_to_history=save_to_history,
    )


def cc(
    field_name: str = "cc",
    value: str = "",
    label="CC",
    type="input",
    required=False,
    default="",
    options=[],
    validator=REGEX.LIST_OF_EMAILS,
    scenario="google_email_send",
    priority=2,
    save_to_history=False,
) -> FieldTemplate:
    return FieldTemplate(
        field_name=field_name,
        value=value,
        label=label,
        type=type,
        required=required,
        default=default,
        options=options,
        validator=validator,
        scenario=scenario,
        priority=priority,
        save_to_history=save_to_history,
    )


def bcc(
    field_name: str = "bcc",
    value: str = "",
    label="BCC",
    type="input",
    required=False,
    default="",
    options=[],
    validator=REGEX.LIST_OF_EMAILS,
    scenario="google_email_send",
    priority=2,
    save_to_history=False,
) -> FieldTemplate:
    return FieldTemplate(
        field_name=field_name,
        value=value,
        label=label,
        type=type,
        required=required,
        default=default,
        options=options,
        validator=validator,
        scenario=scenario,
        priority=priority,
        save_to_history=save_to_history,
    )


def subject(
    field_name: str = "subject",
    value: str = "",
    label="Subject",
    type="input",
    required=True,
    default="",
    options=[],
    validator="",
    scenario="google_email_send",
    priority=2,
    save_to_history=False,
) -> FieldTemplate:
    return FieldTemplate(
        field_name=field_name,
        value=value,
        label=label,
        type=type,
        required=required,
        default=default,
        options=options,
        validator=validator,
        scenario=scenario,
        priority=priority,
        save_to_history=save_to_history,
    )


def body(
    field_name: str = "body",
    value: str = "",
    label="Body",
    type="input",
    required=True,
    default="",
    options=[],
    validator="",
    scenario="google_email_send",
    priority=2,
    save_to_history=False,
) -> FieldTemplate:
    return FieldTemplate(
        field_name=field_name,
        value=value,
        label=label,
        type=type,
        required=required,
        default=default,
        options=options,
        validator=validator,
        scenario=scenario,
        priority=priority,
        save_to_history=save_to_history,
    )


def scope(
    field_name: str = "scope",
    value: str = SCOPES[AllActions.google_send_email],
    label="Scope",
    type="input",
    required=False,
    default="",
    options=[],
    validator="",
    scenario="google_email_send",
    priority=1,
    save_to_history=False,
) -> FieldTemplate:
    return FieldTemplate(
        field_name=field_name,
        value=value,
        label=label,
        type=type,
        required=required,
        default=default,
        options=options,
        validator=validator,
        scenario=scenario,
        priority=priority,
        save_to_history=save_to_history,
    )


def access_token(
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
) -> FieldTemplate:
    return FieldTemplate(
        field_name=field_name,
        value=value,
        label=label,
        type=type,
        required=required,
        default=default,
        options=options,
        validator=validator,
        scenario=scenario,
        priority=priority,
        save_to_history=save_to_history,
    )


def send_email():
    id = 1
    fields = []
    fields.extend([to(), cc(), bcc(), subject(), body(), scope()])

    template = Template(
        id=id,
        provider=provider,
        action_name=AllActions.google_send_email,
        fields=fields,
    )
    return template


def calendar_event():
    pass


fields = {
    "to": to(),
    "cc": cc(),
    "bcc": bcc(),
    "subject": subject(),
    "body": body(),
    "scope": scope(),
    "access_token": access_token(),
}

templates = {AllActions.google_send_email: send_email}
