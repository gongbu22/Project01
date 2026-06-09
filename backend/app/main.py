from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import chat

app = FastAPI()

# CORS 설정
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# chat router 연결
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

@app.get("/")
def root():
  return {"message":"server running"}
