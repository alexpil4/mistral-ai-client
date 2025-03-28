from fastapi import APIRouter, HTTPException
from typing import List
from app.models.schemas import ChatCompletion, ChatCompletionResponse
from app.services.mistral_connector import mistral_chat_completion

router = APIRouter(prefix="/conversation", tags=["Completion"])


@router.post("/", response_model=ChatCompletionResponse)
def complete_chat(message: ChatCompletion):
    chat_completed = mistral_chat_completion(message)
    if not chat_completed:
        raise HTTPException(status_code=422, detail="msg")
    return ChatCompletionResponse(message="Chat completed", data=chat_completed)
