from app.services.embedding_service import create_embedding
from app.services.vector_service import get_collection

# 질문 -> 임베딩 -> 검색

def retrieve_chunks(question: str, n_results: int = 3):

  # Collection 가져오기
  collection = get_collection()

  # 질문을 임베딩
  question_embeddings = create_embedding([question])

  # ChromaDB 검색
  result = collection.query(
    query_embeddings=question_embeddings,
    n_results=n_results   # 기본값 3(위 함수 변수). 이 질문과 가장 비슷한 chunk 3개 찾아줘
  )

  return result