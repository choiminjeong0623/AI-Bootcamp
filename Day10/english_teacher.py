from openai import OpenAI
from dotenv import load_dotenv
import os

from prompt import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

while True:

    try:
        question = input("영어 문장을 입력하세요 (exit 입력 시 종료): ")

        if(question.lower() == "exit"):
            print("프로그램을 종료합니다.")
            break
        
        response = client.responses.create(
            model="gpt-4o-mini",
            input=f"""
            {SYSTEM_PROMPT}

            사용자 문장

            {question}
            """
        )

        print(response.output_text)

        answer = input("\n다른 문장도 연습하시겠습니까?(Y/N)")

        if answer.upper() == "N":
            print("프로그램을 종료합니다.")
            break

    except Exception as e:
        print("오류가 발생했습니다.")
        print(e)