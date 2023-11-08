from .base import create_field_template
from ..constants import SCOPES, REGEX
from ...constants import AllActions
from ...schemas import Template

provider = 'microsoft'


def get_free_or_busy():
    scenario = 'Calendars.Read'
    scope = create_field_template(
        field_name='scope',
        value=SCOPES[AllActions.microsoft_retrieve_free_or_busy_schedule],
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
    schedules = create_field_template(
        field_name='schedules',
        label='Schedules',
        type_of='input',
        required=True,
        scenario=scenario,
        validator=REGEX.SINGLE_OR_MULTIPLE_EMAILS.value
    )

    start_time = create_field_template(
        field_name='start_time',
        label='Start time',
        type_of='input',
        required=True,
        scenario=scenario,
        validator=REGEX.DATETIME
    )
    end_time = create_field_template(
        field_name='end_time',
        label='End time',
        type_of='input',
        required=True,
        scenario=scenario,
        validator=REGEX.DATETIME
    )
    timezone = create_field_template(
        field_name='timezone',
        label='Timezone',
        type_of='input',
        required=True,
        scenario=scenario,
    )

    id = 1
    fields = [
        scope, access_token, schedules, start_time, end_time, timezone
    ]

    template = Template(
        id=id,
        provider=provider,
        action_name=AllActions.microsoft_retrieve_free_or_busy_schedule,
        fields=fields,
    )
    return template
