import requests


class MSGraphClient:
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
            access_token: Access token for the microsoft platform
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
        request_object = {}

        message = {"toRecipients": to, "subject": subject, "body": body}

        if cc:
            message["ccRecipients"] = cc

        if bcc:
            message["bccRecipients"] = bcc

        if attachments:
            message["attachments"] = attachments

        response = requests.post(
            "https://graph.microsoft.com/v1.0/me/sendMail",
            headers=headers,
            json=message,
        )

        return response.json()

