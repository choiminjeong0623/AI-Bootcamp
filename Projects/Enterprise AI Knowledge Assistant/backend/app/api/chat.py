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
from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.core.logger import logger

# ------------------------------------------------
# APIRouter : API를 기능별로 분리하는 객체
# Spring => @RestController
# ------------------------------------------------
router = APIRouter()

@router.post(
    "/chat",
    response_model = ChatResponse
)


# ------------------------------------------------
# Depends : FastAPI의 DI 메커니즘
# FaseAPI가 요청마다 필요한 Session을 생성하고, 함수에 전달한 뒤, 요청이 끝나면 
# 정리(close)까지 담당한다.
# 필요한 객체를  프레임워크가 대신 생성하고 관리해준다.(IoC + DI)
# ------------------------------------------------
def chat(request : ChatRequest, db: Session = Depends(get_db)):

    sentence = request.message

    ## 프롬프트 선택
    if sentence.strip().endswith("?"):
        prompt = CHAT_PROMPT
    else:
        prompt = CORRECTION_PROMPT

    logger.info("Chat request received")

    ## GPT 서비스 호출
    result = get_gpt_response(
        sentence,
        prompt,
        db
    )

    logger.info("Chat response completed")

    return ChatResponse(
        answer=result.answer
    )