from enum import Enum

from src.constants import AllActions

SCOPES = {
    AllActions.microsoft_send_email:
    "https://graph.microsoft.com/v1.0/me/sendMail",
    AllActions.microsoft_retrieve_free_or_busy_schedule:
    "https://graph.microsoft.com/v1.0/me/calendar/getschedule"
}


class REGEX(str, Enum):
    EMPTY_OR_SINGLE_OR_MULTIPLE_EMAILS = r"^(|[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)*@[-!#-\'*+\/-9=?^-~]+(" \
                                         r"?:\.[-!#-\'*+\/-9=?^-~]+)+(?:\s*,\s*[-!#-\'*+\/-9=?^-~]+(?:\.[" \
                                         r"-!#-\'*+\/-9=?^-~]+)*@[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)+)*)$"
    SINGLE_OR_MULTIPLE_EMAILS = r"^([-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)*@[-!#-\'*+\/-9=?^-~]+(?:\.[" \
                                r"-!#-\'*+\/-9=?^-~]+)+(?:\s*,\s*[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)*@[" \
                                r"-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)+)*)$"
    SINGLE_EMAIL = r"^[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)*@[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)+$"
    DATETIME = "^[0-9]{4}\\-[0-9]{1,2}\\-[0-9]{1,2}T[0-9]{1,2}\\:[0-9]{1,2}\\:[0-9]{1,2}(-|\\+)[0-9]{2}\\:[0-9]{2}$"
