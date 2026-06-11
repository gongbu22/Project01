from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import chat
from app.api import upload

app = FastAPI()

# CORS 설정
app.add_middleware(
  CORSMiddleware,
  allow_origins=[
    "http://localhost:5173"
  ],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# router 연결
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])

@app.get("/")
def root():
  return {"message":"server running"}
