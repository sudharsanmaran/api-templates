from src.schemas import FieldTemplate


def create_field_template(
        field_name, label, scenario, value='',
        type_of='input', required=False, default='',
        options=None, validator='', priority=1,
        save_to_history=False
):
    if options is None:
        options = []
    return FieldTemplate(
        field_name=field_name,
        value=value,
        label=label,
        type=type_of,
        required=required,
        default=default,
        options=options,
        validator=validator,
        scenario=scenario,
        priority=priority,
        save_to_history=save_to_history,
    )