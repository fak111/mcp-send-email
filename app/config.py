from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    google_client_id: str = "708919691151-3vgo9cji4u1q790vlvu1t0mnfbt9co78.apps.googleusercontent.com"
    google_client_secret: str = "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"
    api_prefix: str = "/api"
    credentials_file: str = "client_secret_desktop.json"
    scopes: list = ["https://www.googleapis.com/auth/gmail.send"]

settings = Settings()
