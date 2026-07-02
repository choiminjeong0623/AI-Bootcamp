from fastapi import FastAPI
from app.api.chat import router as chat_router

# ------------------------------------------------
# 프로젝트 생성
# Spring => @SpringBootApplication
# ------------------------------------------------
app = FastAPI(
    title="Enterprise AI Knowledge Assistant",
    version="1.0.0"
)

# ------------------------------------------------
# FastAPI는 직적 등록
# Spring에서는 Controller가 자동 등록
# ------------------------------------------------
app.include_router(chat_router)

# ------------------------------------------------
# API 생성
# Spring => @GetMapping
# ------------------------------------------------
@app.get("/")
def root():
    return {
        "message" : "Enterprise AI Knowledge Assistant API"
    }

# ------------------------------------------------
# 서버 상태 확인
# ------------------------------------------------
@app.get("/health")
def health():
    return {
        "status" : "OK"
    }