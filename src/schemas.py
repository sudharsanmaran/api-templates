from typing import List
from pydantic import BaseModel, Field

from src.constants import Status, Types


class FieldTemplate(BaseModel):
    field_name: str = Field(
        ..., description="The name of the field", alias="field_name"
    )
    value: str = Field(
        ..., description="The value of the field", alias="value"
    )
    label: str = Field(
        ...,
        description="The label of the field, used for display purposes",
        alias="label",
    )
    type: Types = Field(
        ..., description="The data type of the field", alias="type"
    )
    required: bool = Field(
        ...,
        description="Indicates whether the field is required",
        alias="required",
    )
    default: str = Field(
        ..., description="The default value of the field", alias="default"
    )
    options: List[str] = Field(
        [],
        description="Possible options for the field if it's a dropdown or \
            similar type",
        alias="options",
    )
    validator: str = Field(
        ...,
        description="The validator of the field in regex format, \
            used for validation purposes",
        alias="validator",
    )
    scenario: str = Field(
        ...,
        description="The scenario in which the field is used",
        alias="scenario",
    )
    priority: int = Field(
        ...,
        description="The priority of the field, used for ordering",
        alias="priority",
    )
    save_to_history: bool = Field(
        ...,
        description="Indicates whether the field value should be \
            saved to history",
        alias="save_to_history",
    )


class Template(BaseModel):
    provider: str = Field(
        ..., description="The provider of the action", alias="provider"
    )
    action_name: str = Field(
        ..., description="The name of the action", alias="action_name"
    )
    fields: list[FieldTemplate] = Field(
        ...,
        description="The list of fields required for the action",
        alias="fields",
    )
    id: int = Field(
        ..., description="The unique identifier of the template", alias="id"
    )


class FormData(BaseModel):
    user_id: int = Field(..., description="The user id", alias="user_id")
    prompt: str = Field(
        ..., description="The prompt of the form", alias="prompt"
    )
    parent_message_id: int = Field(
        ..., description="The parent message id", alias="parent_message_id"
    )
    action_name: str = Field(
        ..., description="The name of the action", alias="action_name"
    )
    fields: list[FieldTemplate] = Field(
        ...,
        description="The list of fields required for the action",
        alias="fields",
    )
    validate_only: bool = Field(
        ...,
        description="Indicates whether the form should be validated only",
        alias="validate_only",
    )
    validate_credentials: bool = Field(
        ...,
        description="Indicates whether the credentials should be validated",
        alias="validate_credentials",
    )


class Form(BaseModel):
    type: str = Field(..., description="The type of the form", alias="type")
    data: FormData = Field(
        ..., description="The data of the form", alias="data"
    )


class ActionsFormData(BaseModel):
    status: Status = Field(
        ..., description="The status of the form", alias="status"
    )
    action_name: str = Field(
        ..., description="The name of the action", alias="action_name"
    )
    prompt: str = Field(
        ..., description="The prompt of the form", alias="prompt"
    )
    fields: list[FieldTemplate] = Field(
        ...,
        description="The list of fields required for the action",
        alias="fields",
    )


class ActionsForm(BaseModel):
    type: str = Field(..., description="The type of the form", alias="type")
    data: ActionsFormData = Field(
        ..., description="The data of the form", alias="data"
    )
