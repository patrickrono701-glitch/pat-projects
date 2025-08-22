import os
from dotenv import load_dotenv
from mistralai import Mistral

# Load API key
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

if not api_key:
    raise RuntimeError("❌ API key not found in .env")

# Initialize client
client = Mistral(api_key=api_key)

# Start conversation history
messages = [{"role": "system", "content": "You are a helpful assistant."}]

print("🤖 Mistral Chat - type 'exit' to quit\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    # Add user message
    messages.append({"role": "user", "content": user_input})

    # Get AI response
    # Get AI response
response = client.chat.complete(
    model="mistral-small",
    messages=messages
)

# Correct way to extract text
ai_message = response.choices[0].message.content
print("Mistral:", ai_message)

# Save assistant reply
messages.append({"role": "assistant", "content": ai_message})
