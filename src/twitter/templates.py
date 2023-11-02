from src.constants import AllActions
from src.schemas import Template, FieldTemplate
from .constants import SCOPES

provider = "twitter"

def scope(
    field_name: str = "scope",
    value: str = SCOPES[AllActions.twitter_read_tweet, AllActions.twitter_write_tweet, AllActions.twitter_users_read],
    label="Scope",
    type="input",
    required=False,
    default="",
    options=[],
    validator="",
    scenario="send_tweet",
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

def access_token(
    field_name="access_token",
    value="",
    label="Access Token",
    type="input",
    required=True,
    default="",
    options=[],
    validator="",
    scenario="twitter_credentials",
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

def text(
    field_name: str = "text",
    value: str = "",
    label="Text",
    type="input",
    required=True,
    default="",
    options=[],
    validator="",
    scenario="send_tweet",
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


def send_tweet():
    id = 1
    fields = [
        text(),
        scope(),
        access_token()
    ]

    template = Template(
        id=id,
        provider=provider,
        action_name=[AllActions.twitter_read_tweet,AllActions.twitter_write_tweet,AllActions.twitter_users_read],
        fields=fields,
    )
    return template



fields = {
    "text": text(),
    "scope": scope(),
    "access_token": access_token(),
}

templates = {
    AllActions.twitter_read_tweet: send_tweet
}