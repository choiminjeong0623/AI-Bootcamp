from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()   # .env 파일을 읽어서 환경변수를 메모리에 올려준다.

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)   # client 객체 생성

response = client.responses.create(
    model="gpt-4o-mini",
    input="안녕하세요! 자기소개를 해주세요."
)

print(response)             # 응답 객체 반환
print(response.output_text)
print(response.id)
print(response.model)