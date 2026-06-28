import chromadb

# ChromaDB가 저장될 폴더
client = chromadb.PersistentClient(path="app/chromadb")

# Collection 생성 ( table 같은거 )
collection = client.get_or_create_collection(
  name="pdf_documents"
)

print("Collection 생성 완료 :)")