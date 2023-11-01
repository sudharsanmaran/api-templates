from enum import Enum
from src.constants import AllActions

SCOPES = {
    AllActions.google_send_email: "https://www.googleapis.com/auth/gmail.send"
}


class REGEX(str, Enum):
    LIST_OF_EMAILS = r"^(|[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)*@[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)+(?:\s*,\s*[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)*@[-!#-\'*+\/-9=?^-~]+(?:\.[-!#-\'*+\/-9=?^-~]+)+)*)$"
