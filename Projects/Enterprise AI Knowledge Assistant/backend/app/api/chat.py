from fastapi import APIRouter

from app.schemas.chat import (
    ChatRequest,
    ChatResponse
)

# ------------------------------------------------
# APIRouter
# Spring => @RestController
# ------------------------------------------------
router = APIRouter()

@router.post(
    "/chat",
    response_model = ChatResponse
)

def chat(request : ChatRequest):
    return ChatResponse(
        answer=f"입력받은 문장 : {request.message}"
    )