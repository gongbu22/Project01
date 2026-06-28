from fastapi import APIRouter, UploadFile, File
import os
from app.services.pdf_service import extract_text_from_pdf
from app.services.text_splitter import split_text

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

  print("===== PDF TEXT =====")
  print(text)
  print("====================")

  return {
    "filename": file.filename,
    # "text_preview": text[:300],
    "chunk_count": len(chunks),
    # "chunks": chunks
    "message": "PDF 업로드 및 텍스트 분할 완료 :)"
  }