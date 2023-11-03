import requests
from fastapi.encoders import jsonable_encoder

from src.microsoft.utils import generateEmailRecipient, generateBody


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

        request_object["toRecipients"] = jsonable_encoder(generateEmailRecipient(toRecipients))
        request_object["subject"] = subject
        request_object["body"] = jsonable_encoder(generateBody(body_content_type, body_content))

        if ccRecipients:
            request_object["ccRecipients"] = jsonable_encoder(generateEmailRecipient(ccRecipients))

        if bccRecipients:
            request_object["bccRecipients"] = jsonable_encoder(generateEmailRecipient(bccRecipients))

        if from_email:
            request_object["from"] = jsonable_encoder(generateEmailRecipient(from_email))
        if saveToSentItems:
            request_object["saveToSentItems"] = bool(saveToSentItems)

        print(request_object)

        response = requests.post(
            "https://graph.microsoft.com/v1.0/me/sendMail",
            headers=headers,
            json=request_object,
        )

        return response.json()

