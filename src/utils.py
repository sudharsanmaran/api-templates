def get_request_body(data):
    body = {}
    for field in data["fields"]:
        body[field["field_name"]] = field["value"]
    return body
