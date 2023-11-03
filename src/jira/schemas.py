from pydantic import Field
from .constants import AssTypeEnum, ProjTempKeyEnum, ProjTypeKeyEnum
from src.schemas import BaseFieldValidations


class JiraBaseFieldValidations(BaseFieldValidations):
    resource_id: str = Field(
        ...,
        description="The unique identifier of the \
        resource",
    )


class CreateProjectRequest(JiraBaseFieldValidations):
    description: str = Field(
        "",
        description="A brief description of the \
        project.",
    )
    key: str = Field(
        ...,
        max_length=10,
        description="Project keys must be unique and start with an uppercase \
            letter followed by one or more uppercase alphanumeric characters.\
                The maximum length is 10 characters.",
    )
    name: str = Field(..., description="The name of the project")
    projectTypeKey: str = Field(
        ProjTypeKeyEnum.SOFTWARE,
        description="The project type key of the project",
    )
    projectTemplateKey: str = Field(
        ProjTempKeyEnum.GREENHOPPER_BASIC,
        description="The project template key of the project",
    )
    assigneeType: str = Field(
        AssTypeEnum.UNASSIGNED,
        description="The assignee type of the project",
    )
    leadAccountId: str = Field(
        ...,
        description="The account ID of the project lead",
    )
