from src.constants import AllActions
from .send_email import send_email
from .get_free_or_busy import get_free_or_busy

templates = {
    AllActions.microsoft_send_email: send_email,
    AllActions.microsoft_retrieve_free_or_busy_schedule: get_free_or_busy,
}