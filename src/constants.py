from enum import Enum


class Types(str, Enum):
    checkbox = "checkbox"
    input = "input"
    dropdown = "dropdown"


class Status(str, Enum):
    success = "success"
    error = "error"
    pending = "pending"


class AllActions(str, Enum):
    # Google Actions
    google_send_email = "GOOGLE_EMAIL_SEND"
    google_create_calendar_event = "GOOGLE_CALENDAR_EVENT_CREATE"

    # Microsoft Actions
    microsoft_send_email = "MICROSOFT_EMAIL_SEND"
    microsoft_create_calendar_event = "MICROSOFT_CALENDAR_EVENT_CREATE"
    
    # Jira Actions
    jira_create_project = "JIRA_PROJECT_CREATE"
