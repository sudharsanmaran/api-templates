from src.google.constants import templates
from src.constants import AllActions
from src.langchain.client import handle_llm_call
from src.microsoft.llm_models import Email


async def fill_send_email(data: dict):
    prompt = data["data"]["prompt"]
    all_fields = data["data"]["fields"]

    llm_fields = ["subject", "body_content"]

    to_generate_content_fields, signature_value = [], None
    for field in all_fields:
        if field["field_name"] in llm_fields and field["value"] == "":
            to_generate_content_fields.append(field)
        if field["field_name"] == "signature":
            signature_value = field["value"]

    if not len(to_generate_content_fields):
        return data

    llm_data = handle_llm_call(
        prompt=prompt,
        model=Email,
        template=templates[AllActions.google_send_email],
        signature=signature_value,
    )

    for field in to_generate_content_fields:
        if field["field_name"] in llm_data:
            field["value"] = llm_data[field["field_name"]]

    return data


formfill_actions = {
    AllActions.microsoft_send_email: fill_send_email,
}
