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

def create_embedding(texts: list[str]) -> list[float]:
  # text를 OpenAI Embedding 으로 변환
  # 여러 개의 text를 한번에 Embedding 하기

  response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
  )

  # embeddings = []

  # for item in response.data:
  #   embeddings.append(item.embedding)

  # return embeddings

# 리스트 컴프리헨션 (List Comprehension)
  return [
    item.embedding
    for item in response.data
  ]