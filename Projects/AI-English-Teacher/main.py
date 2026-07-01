from gpt_service import get_gpt_response
from datetime import datetime
from prompt import (
    CORRECTION_PROMPT,
    CHAT_PROMPT,
)
from database import (
    create_database,
    save_conversation,
    show_recent_conversations,
    search_conversations
)
def classify_input(text):

    if text.strip().endswith("?"):
        return "chat"

    return "correction"

# 프로그램 시작 시 DB 준비
create_database()

print("=" * 40)
print("AI English Teacher")
print("=" * 40)

show_recent_conversations()

while True:

    # if sentence.lower() == "exit":
    #     print("프로그램을 종료합니다.")
    #     break
    print("\n========== 메뉴 ==========")
    print("1. 영어 문장 교정")
    print("2. 최근 대화 보기")
    print("3. 검색")
    print("4. 종료")

    menu = input("메뉴 선택 : ")

    if menu == "1":

        sentence = input("\n영어 문장을 입력하세요 (exit 입력 시 종료): ")
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
    elif menu == "2":
        # 최근 대화 보기
        show_recent_conversations()
    elif menu == "3":
        # 검색하기
        keyword = input("\n검색어를 입력하세요: ")
        rows = search_conversations(keyword)

        if len(rows) == 0:
            print("\n검색 결과가 없습니다.")
        else:
            print("\n===== 검색 결과 =====")

            for row in rows:

                print(f"시간 : {row[2]}")
                print(f"질문 : {row[0]}")
                print(f"답변 :\n{row[1]}")
                print("-" * 50)
    elif menu == "4":
        print("프로그램을 종료합니다.")
        break
