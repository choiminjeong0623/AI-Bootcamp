from app.conversation.history import build_history
from app.core.openai_client import create_response
from app.parser.answer_parser import parse_answer
from app.schemas.gpt_response import GPTResponse

from app.database.database import Base
from app.database.database import engine

from app.repositories.conversation_repository import ConversationRepository
from app.core.logger import logger
from datetime import datetime

# ------------------------------------------------
# Service 역할
# - Message 생성
# - Client 호출
# - Parser 호출
# ------------------------------------------------
def get_gpt_response(sentence, prompt, db):

    messages = [
        {
            "role" : "system",
            "content" : prompt
        }
    ]

    logger.info("Building conversation history")

    # History 생성
    messages.extend(build_history(db))

    logger.info("OpenAI response received")

    #현재 사용자의 입력
    messages.append(
        {
            "role" : "user",
            "content" : sentence
        }
    )

    # GPT 호출
    response = create_response(messages)
    answer = response.output_text

    # 결과 Parsing
    parsed = parse_answer(answer)

    # 저장
    repository = ConversationRepository(db)
    repository.save(
        sentence=sentence,
        answer=answer,
        corrected_sentence=parsed["corrected"],
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    logger.info("Conversation saved")

    # 결과 DTO 반환
    return GPTResponse(
        answer=answer,
        parsed=parsed
    )