from src.jira.constants import AssTypeEnum, JiarScope, ProjTempKeyEnum
from src.schemas import FieldTemplate


def access_token(
    field_name="access_token",
    value="",
    label="Access Token",
    type="input",
    required=False,
    default="",
    options=[],
    validator="",
    scenario="jira_project_create",
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


def resource_id(
    field_name: str = "resource_id",
    value: str = "",
    label="Resources",
    type="dropdown",
    required=True,
    default="",
    options=[],
    validator="",
    scenario="jira_project_create",
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


def scopes(
    field_name="scopes",
    value=f"{JiarScope.BASIC} {JiarScope.WRITE_JIRA_WORK}",
    label="Scopes",
    type="input",
    required=False,
    default="",
    options=[],
    validator="",
    scenario="jira_project_create",
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


def description(
    field_name="description",
    value="",
    label="Description",
    type="input",
    required=False,
    default="",
    options=[],
    validator="",
    scenario="jira_project_create",
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


def key(
    field_name="key",
    value="",
    label="Key",
    type="input",
    required=True,
    default="",
    options=[],
    validator="",
    scenario="jira_project_create",
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


def name(
    field_name="name",
    value="",
    label="Name",
    type="input",
    required=True,
    default="",
    options=[],
    validator="",
    scenario="jira_project_create",
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


def projectTemplateKey(
    field_name="projectTemplateKey",
    value="",
    label="Project Template Key",
    type="dropdown",
    required=True,
    default=ProjTempKeyEnum.GREENHOPPER_BASIC,
    options=[
        ProjTempKeyEnum.GREENHOPPER_BASIC,
        ProjTempKeyEnum.GREENHOPPER_KANBAN,
        ProjTempKeyEnum.GREENHOPPER_SCRUM,
        ProjTempKeyEnum.GREENHOPPER_KANBAN_CLASSIC,
        ProjTempKeyEnum.GREENHOPPER_SCRUM_CLASSIC,
    ],
    validator="",
    scenario="jira_project_create",
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


def leadAccountId(
    field_name="leadAccountId",
    value="",
    label="Lead Account Id",
    type="input",
    required=True,
    default="",
    options=[],
    validator="",
    scenario="jira_project_create",
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


def assigneeType(
    field_name="assigneeType",
    value="",
    label="Assignee Type",
    type="dropdown",
    required=True,
    default=AssTypeEnum.UNASSIGNED,
    options=[
        AssTypeEnum.UNASSIGNED,
        AssTypeEnum.PROJECT_LEAD,
    ],
    validator="",
    scenario="jira_project_create",
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
