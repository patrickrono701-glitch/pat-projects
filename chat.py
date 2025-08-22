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
