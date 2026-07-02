from app.conversation import build_history
from app.core.openai_client import create_response
from app.parser.answer_parser import parse_answer
from app.schemas.gpt_response import GPTResponse

# ------------------------------------------------
# Service 역할
# - Message 생성
# - Client 호출
# - Parser 호출
# ------------------------------------------------
def get_gpt_response(sentence, prompt):

    messages = [
        {
            "role" : "system",
            "content" : prompt
        }
    ]

    messages.extend(build_history())

    #현재 사용자의 입력
    messages.append(
        {
            "role" : "user",
            "content" : sentence
        }
    )
    response = create_response(messages)
    answer = response.output_text
    parsed = parse_answer(answer)

    return GPTResponse(
        answer=answer,
        parsed=parsed
    )