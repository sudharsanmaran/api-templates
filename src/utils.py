from src.constants import AllActions, Status
from src.schemas import ActionsForm, ActionsFormData, FieldTemplate


def get_request_body(data):
    body = {}
    for field in data["data"]["fields"]:
        body[field["field_name"]] = field["value"]
    return body


def get_action_form(
    status: Status,
    action_name: AllActions,
    prompt: str,
    fields: list[FieldTemplate],
) -> ActionsForm:
    return ActionsForm(
        type="Form",
        data=ActionsFormData(
            status=status,
            action_name=action_name,
            prompt=prompt,
            fields=fields,
        ),
    )
