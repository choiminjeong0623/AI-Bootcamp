from pydantic import BaseModel

# ------------------------------------------------
# BaseModel
# Spring => DTO. Request/Response 분리
# ------------------------------------------------
class ChatRequest(BaseModel):
    message : str

class ChatResponse(BaseModel):
    answer : str