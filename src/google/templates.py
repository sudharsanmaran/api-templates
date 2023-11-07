from src.constants import AllActions
from src.schemas import Template, FieldTemplate

from .constants import REGEX, SCOPES, regex_patterns


provider = "google"


def to(
    field_name: str = "to",
    value: str = "",
    label="To",
    type="input",
    required=True,
    default="",
    options=[],
    validator=REGEX.SINGLE_OR_MULTIPLE_EMAILS,
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
    validator=REGEX.EMPTY_OR_SINGLE_OR_MULTIPLE_EMAILS,
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


def from_email(
    field_name: str = "from_email",
    value: str = "",
    label="From Email",
    type="input",
    required=True,
    default="",
    options=[],
    validator=REGEX.SINGLE_EMAIL,
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
    validator=REGEX.EMPTY_OR_SINGLE_OR_MULTIPLE_EMAILS,
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


def signature(
    field_name="signature",
    value="",
    label="Signature",
    type="input",
    required=True,
    default="",
    options=[],
    validator="",
    scenario="google_email_send",
    priority=1,
    save_to_history=False,
) -> FieldTemplate:
    return access_token(
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
    fields = [
        access_token(),
        to(),
        from_email(),
        cc(),
        bcc(),
        subject(),
        body(),
        scope(),
        signature(),
    ]

    template = Template(
        id=id,
        provider=provider,
        action_name=AllActions.google_send_email,
        fields=fields,
    )
    return template


def start(
    field_name: str = "start",
    value: str = "",
    label="Start",
    type="input",
    required=True,
    default="",
    options=[],
    validator=regex_patterns['DATETIME'],
    scenario="google_calendar_event_create",
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


def end(
    field_name: str = "end",
    value: str = "",
    label="End",
    type="input",
    required=True,
    default="",
    options=[],
    validator=regex_patterns['DATETIME'],
    scenario="google_calendar_event_create",
    priority=2,
    save_to_history=False,
) -> FieldTemplate:
    return start(
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


def attendees(
    field_name: str = "attendees",
    value: str = "",
    label="Attendees",
    type="input",
    required=False,
    default="",
    options=[],
    validator=REGEX.SINGLE_OR_MULTIPLE_EMAILS,
    scenario="google_calendar_event_create",
    priority=2,
    save_to_history=False,
) -> FieldTemplate:
    return start(
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


def timezone(
    field_name: str = "timezone",
    value: str = "",
    label="Timezone",
    type="input",
    required=True,
    default="",
    options=[],
    validator="",
    scenario="google_calendar_event_create",
    priority=2,
    save_to_history=False,
) -> FieldTemplate:
    return start(
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


def summary(
    field_name: str = "summary",
    value: str = "",
    label="Summary",
    type="input",
    required=True,
    default="",
    options=[],
    validator="",
    scenario="google_calendar_event_create",
    priority=2,
    save_to_history=False,
) -> FieldTemplate:
    return start(
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


def description(
    field_name: str = "description",
    value: str = "",
    label="Description",
    type="input",
    required=False,
    default="",
    options=[],
    validator="",
    scenario="google_calendar_event_create",
    priority=2,
    save_to_history=False,
) -> FieldTemplate:
    return start(
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


def location(
    field_name: str = "location",
    value: str = "",
    label="Location",
    type="input",
    required=False,
    default="",
    options=[],
    validator="",
    scenario="google_calendar_event_create",
    priority=2,
    save_to_history=False,
) -> FieldTemplate:
    return start(
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


def recurrence(
    field_name: str = "recurrence",
    value: str = "",
    label="Recurrence",
    type="input",
    required=False,
    default="",
    options=[],
    validator="",
    scenario="google_calendar_event_create",
    priority=2,
    save_to_history=False,
) -> FieldTemplate:
    return start(
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


# def reminders(
#     field_name: str = "reminders",
#     value: str = "",
#     label="Reminders",
#     type="input",
#     required=False,
#     default="",
#     options=[],
#     validator="",
#     scenario="google_calendar_event_create",
#     priority=2,
#     save_to_history=False,
# ) -> FieldTemplate:
#     return start(
#         field_name=field_name,
#         value=value,
#         label=label,
#         type=type,
#         required=required,
#         default=default,
#         options=options,
#         validator=validator,
#         scenario=scenario,
#         priority=priority,
#         save_to_history=save_to_history,
#     )


def create_calendar_event():
    id = 2
    fields = [
        access_token(),
        scope(
            value=SCOPES[AllActions.google_create_calendar_event],
            scenario="google_calendar_event_create",
        ),
        start(),
        end(),
        attendees(),
        timezone(),
        summary(),
        description(),
        location(),
        # recurrence(),
    ]

    template = Template(
        id=id,
        provider=provider,
        action_name=AllActions.google_create_calendar_event,
        fields=fields,
    )
    return template


fields = {
    "to": to(),
    "cc": cc(),
    "bcc": bcc(),
    "subject": subject(),
    "body": body(),
    "scope": scope(),
    "access_token": access_token(),
}

templates = {
    AllActions.google_send_email: send_email,
    AllActions.google_create_calendar_event: create_calendar_event,
}
