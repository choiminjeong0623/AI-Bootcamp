import streamlit as st
from datetime import datetime
from gpt_service import get_gpt_response
from prompt import (
    CHAT_PROMPT,
    CORRECTION_PROMPT
)
from database import (
    create_database,
    save_conversation,
    get_recent_conversations,
    search_conversations,
    get_statistics
)

# ------------------------
# Sidebar - 최근 학습
# ------------------------
st.sidebar.title("최근 학습")
rows = get_recent_conversations(limit=5)
# st.write("최근 학습 rows:", rows)

if len(rows) == 0:
    st.sidebar.info("저장된 대화가 없습니다.")
else:
    for row in rows:
        st.sidebar.write(f" {row[0]}")  
        st.sidebar.write(f" {row[1]}")
        st.sidebar.caption(f" {row[2]}")
        st.sidebar.divider()
# ------------------------
# 검색
# ------------------------
st.sidebar.subheader("검색")
keyword = st.sidebar.text_input("검색어를 입력하세요.")

if st.sidebar.button("검색"):
    results = search_conversations(keyword)

    if not results:
        st.sidebar.info("검색 결과가 없습니다.")
    else:
        st.sidebar.success(f"{len(results)}건 검색되었습니다.")

        for row in results:
            with st.sidebar.expander(row[1]):
                st.write("### GPT 답변 ")
                st.write(row[2])

                if row[3]:  # corrected_sentence가 존재할 경우에만 출력
                    st.write("### 교정 문장 ")
                    st.write(row[3])

                st.caption(f"시간 : {row[3]}")

# ------------------------
# 통계
# ------------------------
statics = get_statistics()
st.sidebar.divider()
st.sidebar.subheader("통계")
st.sidebar.metric("총 질문", statics[0])
st.sidebar.write(f"최근 학습 : {statics[1] if statics[1] else '없음'}")


# ------------------------
# DB 생성
# ------------------------
create_database()

# ------------------------
# 질문 / 교정 구분
# ------------------------
def classify_input(text):

    if text.strip().endswith("?"):
        return "chat"

    return "correction"

# --------------------------
# 화면 제목
# --------------------------
st.set_page_config(
    page_title="AI English Teacher",
    page_icon="🤖",
    layout="wide"
)
st.title("AI English Teacher")
st.write("영어 문장을 입력하면 GPT가 교정해줍니다. 질문을 입력하면 GPT가 답변해줍니다.")
# --------------------------
# 입력창
# --------------------------
sentence = st.text_area("영어 문장을 입력하세요.", height=150)

# --------------------------
# 버튼
# --------------------------
if st.button("교정하기"):
    if sentence.strip() == "":
        st.warning("영어 문장을 입력해주세요.")
    else:
        intent = classify_input(sentence)

        if intent == "chat":
            prompt = CHAT_PROMPT
        else:
            prompt = CORRECTION_PROMPT
        
        with st.spinner("GPT가 응답을 생성하는 중입니다..."):
            answer, corrected_sentence = get_gpt_response(sentence, prompt)
        
        # --------------------------
        # 현재 시간
        # --------------------------
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # --------------------------
        # SQLite 저장
        # --------------------------
        save_conversation(
            sentence=sentence, 
            answer=answer, 
            corrected_sentence=corrected_sentence, 
            time=time
        )

        st.success("학습 내용이 저장되었습니다.")
        st.divider()
        st.subheader("GPT 답변")
        st.write(answer)

        if corrected_sentence:
            st.subheader("교정 문장")
            print("교정 문장:", corrected_sentence)
            st.write(corrected_sentence)
        
