from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model="gpt-4o",
  temperature=0.9,
  messages=[
    {"role": "system", "content": "배우 이광수가 재석이형을 부르는 말투로 해줘"},
    {"role": "user", "content": "오늘 날짜가 뭐야?"},
  ]
)

print(response.choices[0].message.content)