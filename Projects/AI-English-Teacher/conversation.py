import json
import os

FILE_NAME = "conversation_log.json"

## 대화 저장하기
def save_conversation(sentence, answer, corrected_sentence, time):

    # data = []

    # if os.path.exists(FILE_NAME):
    #     try:
    #         with open(FILE_NAME, "r", encoding="utf-8") as file:
    #             data = json.load(file)
    #     except (FileNotFoundError, json.JSONDecodeError):
    #             data = []
    # else:
    #     data = []
    
    # data.append({
    #     "sentence" : sentence,
    #     "answer" : answer,                          # 사용자에게 보여줄 전체 답변
    #     "corrected_sentence" : corrected_sentence,  # GPT 기억용
    #     "time" : time
    # })

    # with open(FILE_NAME, "w", encoding="utf-8") as file:
    #     json.dump(
    #         data,
    #         file,
    #         ensure_ascii=False,
    #         indent=4
    #     )
    
    # JSON 파일 대신 SQLite 데이터베이스에 대화 저장
    connection = sqlite3.connect("english_teacher.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO conversation (question, answer, corrected_sentence, created_at)
        VALUES(?, ?, ?, ?)
        """,
        (sentence, answer, corrected_sentence, time)
    )
    connection.commit()
    connection.close()

## 대화 기록 불러오기
def load_conversations():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

## 최근 대화 출력하기
def show_recent_conversations(count=5):
#     data = load_conversations()

#     if not data:
#         print("저장된 대화가 없습니다.")
#         return
    
#     print("\n===== 최근 대화 =====")

#     for conversation in data[-count:]:
#         print(f"시간 : {conversation['time']}")
#         print(f"질문 : {conversation['sentence']}")
#         print(f"답변 : {conversation['answer']}")
#         print("-" * 40)

# ## 최근 N개만 가져오기
# def get_recent_conversations(limit=5):
#     conversations  = load_conversations()
#     return conversations[-limit:]

# ## GPT에게 보낼 대화 기록 생성
# def build_history(limit=5):
    
#     history = []

#     conversations = get_recent_conversations(limit) 

#     for c in conversations:
#         history.append({
#             "role" : "user",
#             "content" : c["sentence"]
#         })

#         history.append({
#             "role" : "assistant",
#             "content" : c["corrected_sentence"]
#         })
    
#     return history

## JSON 파일 대신 SQLite 데이터베이스에 저장된 최근 대화 출력하기
connection = sqlite3.connect("english_teacher.db")
curosr = connection.cursor()

cursor.execute(
    """
        SELECT question, created_at FROM conversation
        ORDER BY id DESC
        LIMIT 5
    """
)

row = cursor.fetchall()

print("=" * 50)
print("최근 학습 기록")
print("=" * 50)

for row in rows:
    print()
    print("시간")
    print(row[1])
    print()
    print("질문")
    print(row[0])
    print("-" * 50)

connection.close()