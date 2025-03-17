from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
import os
import pickle
from ..config import settings

class EmailService:
    def __init__(self):
        self.creds = None
        self.token_file = "token.pickle"
        self.initialize_credentials()

    def initialize_credentials(self):
        if os.path.exists(self.token_file):
            with open(self.token_file, 'rb') as token:
                self.creds = pickle.load(token)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    settings.credentials_file, settings.scopes)
                self.creds = flow.run_local_server(port=8001)

            with open(self.token_file, 'wb') as token:
                pickle.dump(self.creds, token)

    def create_message(self, to: str, content: str):
        message = MIMEText(content)
        message['to'] = to
        message['subject'] = 'MCP Email Service'
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
        return {'raw': raw_message}

    async def send_email(self, to: str, content: str):
        try:
            service = build('gmail', 'v1', credentials=self.creds)
            message = self.create_message(to, content)
            sent_message = service.users().messages().send(
                userId='me', body=message).execute()
            return {"status": "success", "message": f"Email sent successfully. Message ID: {sent_message['id']}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
