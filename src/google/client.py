import requests


class GmailClient:
    def send_email(
        self,
        access_token,
        to,
        subject,
        body,
        attachments=None,
        cc=None,
        bcc=None,
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

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        message = {"to": to, "subject": subject, "body": body}

        if cc:
            message["cc"] = cc

        if bcc:
            message["bcc"] = bcc

        if attachments:
            message["attachments"] = attachments

        response = requests.post(
            "https://www.googleapis.com/gmail/v1/users/me/messages",
            headers=headers,
            json=message,
        )

        return response.json()


class CalendarClient:
    def create_calendar_event(
        self, access_token, summary, description, start, end
    ):
        """Creates a calendar event using the Calendar API.

        Args:
            summary: The summary of the event.
            description: The description of the event.
            start: The start date and time of the event.
            end: The end date and time of the event.

        Returns:
            A JSON object representing the created event.
        """

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        event = {
            "summary": summary,
            "description": description,
            "start": start,
            "end": end,
        }

        response = requests.post(
            "https://www.googleapis.com/calendar/v3/calendars/primary/events",
            headers=headers,
            json=event,
        )

        return response.json()


class Client(GmailClient, CalendarClient):
    pass
