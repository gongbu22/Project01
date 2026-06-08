from email import message
from unittest.mock import Base

from fastapi import APIRouter
from pydantic import BaseModel

from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 불러오기
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

router = APIRouter()

# 요청 데이터 형식
class ChatRequest(BaseModel):
  message: str

@router.post("/")
async def chat(request: ChatRequest):

  response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.9,
    messages=[
      {
        "role": "system",
        "content": "배우 이광수가 재석이형을 부르는 말투로 해줘"
      },
      {
        "role": "user",
        "content": request.message
      },
    ]
  )

  return {
    "answer": response.choices[0].message.content
  }

# print(response.choices[0].message.content)