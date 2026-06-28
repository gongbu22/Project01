import chromadb

# ChromaDB 연결
client = chromadb.PersistentClient(path="app/chromadb")


def get_collection():
  # pdf_documents Collection을 반환

  return client.get_or_create_collection(
    name="pdf_documents"
  )

# def test_insert():
#   collection = get_collection()

#   collection.add(
#     documents=[
#       "FastAPI는 Python 웹 프레임워크입니다."
#     ],
#     embeddings=[
#       [0.1, 0.2, 0.3]
#     ],
#     metadatas=[
#       {
#         "filename": "test.pdf",
#         "page": 1
#       }
#     ],
#     ids=[
#       "test1"
#     ]
#   )


# print("저장 완료 :)")