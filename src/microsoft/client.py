import requests
from fastapi.encoders import jsonable_encoder

from src.microsoft.utils import generateEmailRecipient, generateBody, del_none, get_date_with_time_zone


class MSGraphClient:
    def send_email(
        self,
        access_token,
        toRecipients,
        subject,
        body_content_type,
        body_content,
        ccRecipients=None,
        bccRecipients=None,
        from_email=None,
        saveToSentItems=None
    ):
        """Sends an email using the Gmail API.

        Args:
            access_token: Access token for the microsoft platform
            toRecipients: A list of email addresses to send the email to.
            subject: The subject of the email.
            body_content_type: The body type of email, it can be text or html
            body_content: The body of the email
            ccRecipients: A list of email addresses to send the email \
                to as CC recipients.
            bccRecipients: A list of email addresses to send the email \
                to as BCC recipients.
            from_email: email address of sender.
            saveToSentItems: Indicates whether to save the message in Sent Items.

        Returns:
            A JSON object representing the sent email.
        """

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        request_object = dict()
        message = dict()

        print('Came here')

        message["toRecipients"] = [del_none(jsonable_encoder(generateEmailRecipient(toRecipients)))]
        message["subject"] = subject
        message["body"] = del_none(jsonable_encoder(generateBody(body_content_type, body_content)))

        if ccRecipients:
            message["ccRecipients"] = [del_none(jsonable_encoder(generateEmailRecipient(ccRecipients)))]

        if bccRecipients:
            message["bccRecipients"] = [del_none(jsonable_encoder(generateEmailRecipient(bccRecipients)))]

        if from_email:
            message["from"] = del_none(jsonable_encoder(generateEmailRecipient(from_email)))

        request_object['message'] = message
        if saveToSentItems:
            request_object["saveToSentItems"] = bool(saveToSentItems)

        print(request_object)

        response = requests.post(
            "https://graph.microsoft.com/v1.0/me/sendMail",
            headers=headers,
            json=request_object,
        )
        if response.status_code == 202:
            return {}
        print(response.json())

        return response.json()

    @staticmethod
    def get_free_or_busy_schedule(access_token: str,
                                  schedules: str,
                                  start_time: str,
                                  end_time: str,
                                  timezone: str
                                  ):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        request_object = dict()

        request_object['Schedules'] = [schedules]
        request_object['StartTime'] = jsonable_encoder(get_date_with_time_zone(start_time, timezone))
        request_object['EndTime'] = jsonable_encoder(get_date_with_time_zone(end_time, timezone))

        response = requests.post(
            "https://graph.microsoft.com/v1.0/me/calendar/getschedule",
            headers=headers,
            json=request_object,
        )
        if response.status_code == 202:
            return {}
        print(response.json())

        return response.json()



