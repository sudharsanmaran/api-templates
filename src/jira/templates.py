from src.schemas import Template
from src.constants import AllActions
from src.jira.fields.project import (
    access_token,
    scopes,
    resource_id,
    name,
    key,
    description,
    projectTemplateKey,
    leadAccountId,
)


provider = "jira"


def create_project():
    template = Template(
        id=3,
        provider=provider,
        action_name=AllActions.jira_create_project,
        fields=[
            access_token(),
            scopes(),
            resource_id(),
            name(),
            key(),
            description(),
            projectTemplateKey(),
            leadAccountId(),
            # assigneeType(),
        ],
    )
    return template


templates = {AllActions.jira_create_project: create_project}
