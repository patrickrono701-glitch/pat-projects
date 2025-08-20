import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise RuntimeError("❌ API key not found in .env")

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": "Hello from my script!"}],
)

print("AI Response:", chat_response.choices[0].message.content)
