from src.jira.constants import JiarScope
from src.schemas import FieldTemplate, Template
from src.constants import AllActions


provider = "jira"


def create_project():
    id = 1
    scenario = "jira_create_project"
    scopes = FieldTemplate(
        field_name="scopes",
        value=JiarScope.BASIC,
        label="Scopes",
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
    description = FieldTemplate(
        field_name="description",
        value="",
        label="Description",
        type="input",
        required=False,
        default="",
        options=[],
        validator="",
        scenario=scenario,
        priority=2,
        save_to_history=False,
    )
    key = FieldTemplate(
        field_name="key",
        value="",
        label="Key",
        type="input",
        required=True,
        default="",
        options=[],
        validator="",
        scenario=scenario,
        priority=2,
        save_to_history=False,
    )
    name = FieldTemplate(
        field_name="name",
        value="",
        label="Access Token",
        type="input",
        required=True,
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
        action_name=AllActions.jira_create_project,
        fields=[scopes, access_token, description, key, name],
    )
    return template


templates = {AllActions.jira_create_project: create_project}
