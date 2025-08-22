import os
import time
import requests
from bs4 import BeautifulSoup
from mistralai import Mistral
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise RuntimeError("❌ API key not found in .env")

client = Mistral(api_key=api_key)

# ---------- GOOGLE SEARCH (FAST) ----------
def google_search(query):
    """Fetch top Google result snippet using requests (fast)."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        url = f"https://www.google.com/search?q={query}"
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        snippet_elem = soup.select_one(".BNeawe")
        if snippet_elem:
            return snippet_elem.text
        else:
            return "⚠️ No snippet found (Google layout changed)."
    except Exception as e:
        return f"⚠️ Error fetching data: {e}"


# ---------- SAFE CHAT ----------
def safe_chat(client, messages, retries=3):
    models = ["mistral-large-latest", "mistral-medium-latest", "mistral-small-latest"]
    for attempt in range(retries):
        for model in models:
            try:
                response = client.chat.complete(model=model, messages=messages)
                return response.choices[0].message.content
            except Exception as e:
                print(f"⚠️ {model} failed: {e}. Retrying...")
                time.sleep(2 ** attempt)
    return "❌ All models failed after retries."

# ---------- MAIN CHAT LOOP ----------
print("🤖 Realtime Chat - type 'exit' to quit")
conversation = []

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break

    # Pull realtime data fast
    live_data = google_search(user_input)

    conversation.append({
        "role": "user",
        "content": f"{user_input}\n(Live data: {live_data})"
    })

    ai_message = safe_chat(client, conversation)
    print(f"AI: {ai_message}")

    conversation.append({"role": "assistant", "content": ai_message})
