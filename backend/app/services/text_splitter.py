def split_text(text: str, chunk_size: int = 500) -> list[str]:
  # 텍스트를 chunk_size 크기만큼 잘라 리스트로 반환

  chunks = []

  for i in range(0, len(text), chunk_size):
    chunks.append(text[i:i + chunk_size])
  
  return chunks