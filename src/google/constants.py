from enum import Enum
from src.constants import AllActions

SCOPES = {
    AllActions.google_send_email: "https://www.googleapis.com/auth/gmail.send",
    # AllActions.google_create_calendar_event: "https://www.googleapis.com/auth/calendar.events",
}


# flake8: noqa
class REGEX(str, Enum):
    EMPTY_OR_SINGLE_OR_MULTIPLE_EMAILS = r"^(|[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)*@[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)+(?:\s*,\s*[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)*@[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)+)*)$"
    SINGLE_OR_MULTIPLE_EMAILS = r"^([-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)*@[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)+(?:\s*,\s*[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)*@[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)+)*)$"
    SINGLE_EMAIL = r"^[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)*@[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)+$"
    DATETIME = r"\d{4}-\d{2}-\d{2}(?:\s\d{2}:\d{2}:\d{2})?"

