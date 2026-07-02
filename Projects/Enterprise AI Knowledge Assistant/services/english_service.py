from datetime import datetime
from database import save_conversation
from prompt import (
    CHAT_PROMPT,
    CORRECTION_PROMPT
)
from modes.english_mode import EnglishMode

#######################################
# 이름 : English_service 
# 역할 : GPT 호출, DB 저장
#######################################

def process_english(sentence):

    mode = EnglishMode()

    prompt = mode.get_prompt(sentence)

    answer, parsed = get_gpt_response(sentence, prompt)
    
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
        corrected_sentence=parsed["corrected"], 
        time=time
    )

    return answer, parsed