from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

## OpenAI SDK 역할 수행
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def create_response(messages):
    return client.responses.create(
        model="gpt-4.1-mini",
        input=messages
    )