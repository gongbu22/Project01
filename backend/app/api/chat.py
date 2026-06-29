from email import message
from unittest.mock import Base

from fastapi import APIRouter
from pydantic import BaseModel

from openai import OpenAI
from dotenv import load_dotenv
import os

from app.services.retrieval_service import retrieve_chunks


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

  result = retrieve_chunks(request.message)

  # print("="*50)
  # print(result)
  # print("="*50)

  documents = result["documents"][0]
  context = "\n\n".join(documents) 

  response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.9,
    messages=[
      {
        "role": "system",
        "content": f""" 
          너는 PDF를 참고해서 답변하는 AI야.

          반드시 아래 문서를 참고해서 답변해.

          문서: {context}

          문서에 없는 내용은 '문서에서 찾을 수 없습니다.' 라고 대답해.

          그리고 말투는 지적이면서 단호한 말투로 해줘
        """
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