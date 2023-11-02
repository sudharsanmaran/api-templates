from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.constants import AllActions, Status
from src.schemas import Template, Form, ActionsForm
from src.google.actions import actions as google_actions
from src.google.templates import templates as google_templates
from src.microsoft.actions import actions as microsoft_actions
from src.microsoft.templates import templates as microsoft_templates
from src.jira.actions import actions as jira_actions
from src.jira.templates import templates as jira_templates

all_actions = {**google_actions, **jira_actions, **microsoft_actions}

all_templates = {**google_templates, **jira_templates, **microsoft_templates}


router = APIRouter(prefix="/api/v1")


@router.get("/templates/{action_name}")
def get_template(action_name: AllActions) -> Template:
    """Gets the template for the specified action."""
    return all_templates.get(action_name.value)()


@router.post("/forms/apply", response_model=ActionsForm)
def apply_form(data: Form):
    """Applies the form."""
    result = all_actions.get(data.data.action_name)(data.model_dump())
    if result.data.status == Status.error:
        return JSONResponse(content=result.model_dump(), status_code=400)
    return JSONResponse(content=result.model_dump(), status_code=200)


@router.post("/forms/fill")
def fill_form(data: Form) -> Form:
    """Fills the form."""
    # TODO: fill user specific info
    return None
