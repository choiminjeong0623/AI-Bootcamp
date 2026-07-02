from openai import OpenAI
from dotenv import load_dotenv
from app.core.config import settings
from app.core.logger import logger
import os

load_dotenv()

## OpenAI SDK 역할 수행
client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

def create_response(messages):
    try:
        logger.info("Sending request to OpenAI")
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=messages
        )
        logger.info("OpenAI completed")
    except Exception as e:
        logger.exception(e)
        raise

    return response