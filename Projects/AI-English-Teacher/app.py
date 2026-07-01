import streamlit as st
from gpt_service import get_gpt_response
from prompt import (
    CHAT_PROMPT,
    CORRECTION_PROMPT
)

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
        
        st.subheader("완료")
        st.divider()
        st.subheader("GPT 답변")
        st.write(answer)

        if corrected_sentence:
            st.subheader("교정 문장")
            print("교정 문장:", corrected_sentence)
            st.write(corrected_sentence)
        
