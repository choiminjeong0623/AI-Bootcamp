from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


while True:
    question = input("질문을 입력하세요 : ")

    if(question.lower() == 'exit'):
        print("openAI가 종료됩니다.")
        break
    try:    
        response = client.responses.create(
        model="gpt-4o-mini",
        input=question
        )

        print("\n===== GPT ======")
        print(response.output_text)

    except Exception as e:
        print("오류가 발생했습니다.")
        print(e)

    


  

# print(response)