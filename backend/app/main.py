from fastapi import FastAPI

from app.api import chat

app = FastAPI()

# chat router 연결
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

@app.get("/")
def root():
  return {"message":"server running"}
