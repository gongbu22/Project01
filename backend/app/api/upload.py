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
  for index, chunk in enumerate(chunks):
    embedding = create_embedding(chunk)

    save_chunk(
      chunk=chunk,
      embedding=embedding,
      filename=file.filename,
      chunk_index=index
    )

  print("모든 Chunk 저장 완료!! :)")