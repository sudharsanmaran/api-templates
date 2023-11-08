import base64
from typing import List
from email.message import EmailMessage
import logging
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.errors import Error


logger = logging.getLogger(__name__)


class GmailClient:
    def send_email(
        self,
        access_token,
        to: List[str],
        from_email,
        subject,
        body,
        attachments=None,
        cc: List[str] = [],
        bcc: List[str] = [],
    ):
        """Sends an email using the Gmail API.

        Args:
            to: A list of email addresses to send the email to.
            subject: The subject of the email.
            body: The body of the email.
            attachments: A list of attachments to include in the email. \
                Each attachment should be a dictionary with the following keys:
                * mimeType: The MIME type of the attachment.
                * attachment: The base64 encoded attachment data.
            cc: A list of email addresses to send the email \
                to as CC recipients.
            bcc: A list of email addresses to send the email \
                to as BCC recipients.

        Returns:
            A JSON object representing the sent email.
        """

        try:
            credentials = Credentials(access_token)
            service = build("gmail", "v1", credentials=credentials)

            message = EmailMessage()

            message.set_content(body)

            message["To"] = to
            message["From"] = from_email
            message["Subject"] = subject
            if cc:
                message["Cc"] = cc
            if bcc:
                message["Bcc"] = bcc

            encoded_message_bytes = message.as_bytes()
            encoded_message = base64.urlsafe_b64encode(
                encoded_message_bytes
            ).decode()

            message_to_send = {"raw": encoded_message}

            send_message = (
                service.users()
                .messages()
                .send(userId="me", body=message_to_send)
                .execute()
            )
            logger.info(f'Message Id: {send_message["id"]}')
        except Error as error:
            logger.error(error)
            raise error
        return send_message


class CalendarClient:
    def create_calendar_event(
        self,
        access_token,
        summary,
        description,
        attendees,
        start,
        end,
        location,
        timezone,
    ):

        try:
            credentials = Credentials(access_token)
            service = build("calendar", "v3", credentials=credentials)

            """
                    event = {
        'summary': 'Google I/O 2015',
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '2015-05-28T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2015-05-28T17:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': [
            {'email': 'lpage@example.com'},
            {'email': 'sbrin@example.com'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
                    """

            event = {
                "start": {
                    "dateTime": start,
                    "timeZone": timezone,
                },
                "end": {
                    "dateTime": end,
                    "timeZone": timezone,
                },
                "summary": summary,
                "description": description,
                "attendees": [{"email": attendee} for attendee in attendees],
                "location": location,

            }

            event = (
                service.events()
                .insert(calendarId="primary", body=event)
                .execute()
            )
            logger.info(f'Event Id: {event["id"]}')
        except Error as error:
            logger.error(error)
            raise error
        return event


class ContactClient:
    pass


class Client(GmailClient, CalendarClient):
    pass
