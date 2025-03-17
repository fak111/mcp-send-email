from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from .services.email_service import EmailService
from .config import settings

app = FastAPI(title="MCP Email Service")
email_service = EmailService()

class EmailRequest(BaseModel):
    address: EmailStr
    content: str

@app.post(f"{settings.api_prefix}/send-email")
async def send_email(request: EmailRequest):
    result = await email_service.send_email(request.address, request.content)
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["message"])
    return result
