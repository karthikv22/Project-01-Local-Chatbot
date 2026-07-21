from ollama import chat

messages = []

print("=" * 50)
print("🤖 Local AI Chatbot (Qwen3)")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = chat(
        model="qwen3:8b",
        messages=messages
    )

    answer = response["message"]["content"]

    print("\nAI:", answer)

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )