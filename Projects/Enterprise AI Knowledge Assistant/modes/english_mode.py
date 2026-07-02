from prompt import (
    CHAT_PROMPT,
    CORRECTION_PROMPT
)

# ------------------------
# 입력 시 Prompt 선택
# ------------------------
class EnglishMode:
    def get_prompt(self, sentence):

        if sentence.strip().endswith("?"):
            return CHAT_PROMPT
        
        return CORRECTION_PROMPT