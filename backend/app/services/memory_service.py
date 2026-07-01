from app.services.embedding_service import create_embedding
from app.services.vector_service import get_chat_collection

def save_chat(question:str, answer: str):
  collection = get_chat_collection()

  # 저장할 문서
  document = f"""
    User: {question}
    Assistant: {answer}
  """

  # 임베딩 생성
  embedding = create_embedding([document])[0]

  # 저장
  collection.add(
    ids=[f"chat_{collection.count()}"],
    documents=[document],
    embeddings=[embedding],
    metadatas=[
      {
        "type": "chat"
      }
    ]
  )