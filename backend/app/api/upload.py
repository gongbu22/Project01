from fastapi import APIRouter, UploadFile, File
import os
from app.services.pdf_service import extract_text_from_pdf
from app.services.text_splitter import split_text
from app.services.vector_service import save_chunk
from app.services.embedding_service import create_embedding


router = APIRouter()

UPLOAD_DIR = "app/uploads"

@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
  file_path = os.path.join(UPLOAD_DIR, file.filename)

  # 파일 저장
  with open(file_path, "wb") as f:
    f.write(await file.read())

  # 텍스트 추출
  text = extract_text_from_pdf(file_path)

  chunks = split_text(text)

  # embedding 후 chromadb에 저장

  embeddings = create_embedding(chunks)

  # 번호가 필요해서 enumerate 사용
  # zip(chunks, embeddings) ===>  ex) (testText, [0.1,0.2])
  for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

    save_chunk(
      chunk=chunk,
      embedding=embedding,
      filename=file.filename,
      chunk_index=index
    )

  print("모든 Chunk 저장 완료!! :)")