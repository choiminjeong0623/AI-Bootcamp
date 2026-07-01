from openai import OpenAI
from dotenv import load_dotenv
from conversation import build_history
from pprint import pprint
from prompt import (
    CORRECTION_PROMPT,
    CHAT_PROMPT,
)
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# GPT 응답 생성
def get_gpt_response(sentence, prompt):

    if prompt == CORRECTION_PROMPT:
        corrected_sentence = CORRECTION_PROMPT
    else:
        corrected_sentence = CHAT_PROMPT
        
    messages = [
        {
            "role" : "system",
            "content" : corrected_sentence
        }
    ]

    # 이전 대화 추가
    messages.extend(build_history())

    #현재 사용자의 입력
    messages.append(
        {
            "role" : "user",
            "content" : sentence
        }
    )

    # pprint(build_history())

    response = client.responses.create(
        model = "gpt-4o-mini",
        input = messages
    )

    # 디버깅 시 사용
    # from pprint import pprint
    # pprint(response)

    answer = response.output_text
    corrected_sentence = get_corrected_sentence(answer)
    parsed = parse_answer(answer)

    return answer, corrected_sentence, parsed

## GPT 응답에서 수정된 문장만 추출
def get_corrected_sentence(answer):
    # print("===== answer =====")
    # print(answer)

    lines = [
        line.strip()
        for line in answer.split("\n")
        if line.strip()
    ]

    # print("===== lines =====")
    # print(lines)

    return lines[1]

def parse_answer(answer):
    result = {
        "corrected_answer" : "",
        "reason" : "",
        "translation" : "",
        "better" : ""
    }

    current = None

    for line in answer.split("\n"):
        line = line.strip()

        if not line:
            continue

        if "[수정된 문장]" in line:
            current = "corrected_answer"
            continue
        elif "[수정 이유]" in line:
            current = "reason"
            continue
        elif "[한국어 번역]" in line:
            current = "translation"
            continue
        elif "[더 좋은 표현]" in line:
            current = "better"
            continue
        
        if current:
            result[current] += line + "\n"
    
    return result