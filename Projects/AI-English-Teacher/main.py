from gpt_service import get_gpt_response
from datetime import datetime
from conversation import (
    save_conversation
    , show_recent_conversations
)
from prompt import (
    CORRECTION_PROMPT,
    CHAT_PROMPT,
)

def classify_input(text):

    if text.strip().endswith("?"):
        return "chat"

    return "correction"

print("=" * 40)
print("AI English Teacher")
print("=" * 40)

show_recent_conversations()

while True:
    sentence = input("\n영어 문장을 입력하세요 (exit 입력 시 종료): ")

    if sentence.lower() == "exit":
        print("프로그램을 종료합니다.")
        break

    # GPT 응답 생성
    intent = classify_input(sentence)

    if intent == "chat":
        prompt = CHAT_PROMPT
    else:
        prompt = CORRECTION_PROMPT
        
    answer, corrected_sentence = get_gpt_response(sentence, prompt)
    # 현재 시간
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 화면 출력
    print("\n===== GPT =====")
    print(answer)
    print(time)

    # 대화 저장
    save_conversation(
        sentence=sentence, 
        answer=answer, 
        corrected_sentence=corrected_sentence, 
        time=time)