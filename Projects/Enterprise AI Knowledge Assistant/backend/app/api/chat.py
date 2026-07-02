from fastapi import APIRouter

from app.schemas.chat import (
    ChatRequest,
    ChatResponse
)
from app.services.gpt_service import get_gpt_response

from app.core.prompt import (
    CHAT_PROMPT,
    CORRECTION_PROMPT
)
from app.parser.answer_parser import parse_answer
# ------------------------------------------------
# APIRouter : API를 기능별로 분리하는 객체
# Spring => @RestController
# ------------------------------------------------
router = APIRouter()

@router.post(
    "/chat",
    response_model = ChatResponse
)

def chat(request : ChatRequest):

    sentence = request.message

    ## 프롬프트 선택
    if sentence.strip().endswith("?"):
        prompt = CHAT_PROMPT
    else:
        prompt = CORRECTION_PROMPT

    ## GPT 서비스 호출
    result = get_gpt_response(
        sentence,
        prompt
    )

    return ChatResponse(
        answer=result.answer
    )