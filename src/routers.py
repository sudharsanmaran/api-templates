from fastapi import APIRouter

from src.constants import AllActions
from src.schemas import Template, Form, ActionsFormData
from src.google.actions import actions as google_actions
from src.google.templates import templates as google_templates
from src.jira.actions import actions as jira_actions
from src.jira.templates import templates as jira_templates

all_actions = {**google_actions, **jira_actions}

all_templates = {**google_templates, **jira_templates}


router = APIRouter(prefix="/api/v1")


@router.get("/templates/{action_name}")
def get_template(action_name: AllActions) -> Template:
    """Gets the template for the specified action."""
    return all_templates.get(action_name.value)()


@router.post("/forms/apply")
def apply_form(data: Form) -> ActionsFormData:
    """Applies the form."""
    result = all_actions.get(data.data.action_name)(data.model_dump())
    return result


@router.post("/forms/fill")
def fill_form(data: Form) -> Form:
    """Fills the form."""
    # TODO: fill user specific info
    return None
