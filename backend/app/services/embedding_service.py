from pydoc import cli
from urllib import response

from openai import OpenAI
from dotenv import load_dotenv

import os

# 텍스트 -> 벡터 변환만 한다. (임베딩)

# .env 읽기
load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

def create_embedding(text: str) -> list[float]:
  # text를 OpenAI Embedding 으로 변환

  response = client.embeddings.create(
    model="text-embedding-3-small",
    input=text
  )

  return response.data[0].embedding