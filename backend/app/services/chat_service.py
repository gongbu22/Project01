from openai import OpenAI
from dotenv import load_dotenv
import os

from app.services.retrieval_service import retrieve_chunks

load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

def chat_with_rag(question: str):

  # ChromaDB 검색
  result = retrieve_chunks(question)

  # 검색된 문서
  documents = result["documents"][0]

  # 하나의 문자열로 합치기
  context = "\n\n".join(documents)

  # gpt 호출
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

  return response.choices[0].message.content 