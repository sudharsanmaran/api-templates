from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.constants import AllActions, Status
from src.schemas import Template, Form, ActionsForm
from src.google.actions import actions as google_actions
from src.google.templates import templates as google_templates
from src.google.formfill import formfill_actions as google_formfill_actions
from src.microsoft.formfill import formfill_actions as microsoft_formfill_actions
from src.microsoft.actions import actions as microsoft_actions
from src.microsoft.templates import templates as microsoft_templates
from src.jira.actions import actions as jira_actions
from src.jira.templates import templates as jira_templates
from src.jira.formfill import formfills as jira_formfill
from src.twitter.actions import actions as twitter_actions
from src.twitter.templates import templates as twitter_templates

all_actions = {
    **google_actions,
    **jira_actions,
    **microsoft_actions,
    **twitter_actions,
}

all_templates = {
    **google_templates,
    **microsoft_templates,
    **twitter_templates,
    **jira_templates,
}

all_fillform_actions = {
    **jira_formfill,
    **google_formfill_actions,
    **microsoft_formfill_actions
}

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
async def fill_form(data: Form) -> Form:
    """Fills the form."""
    result = await all_fillform_actions.get(data.data.action_name)(
        data.model_dump()
    )
    return result
