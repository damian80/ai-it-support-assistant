import anthropic
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

conversation=[]
print("Welcome to AI IT Support Assistant")
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ")
    if user_input == "quit":
        break
    if user_input == "":
        continue

    conversation.append({"role": "user", "content": user_input})
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        system="You are an IT support assistant for a school. The school uses macOS,Windows 11, JAMF Pro for device management, and Google Workspace. Be helpful, concise and professional.",
        messages=conversation
    )


    conversation.append({"role": "assistant", "content": message.content[0].text})
    print(f"\nIT Support: {message.content[0].text}\n")
with open("conversation_log.txt", "w") as file:
    file.write(f"Conversation date: {datetime.now()}\n\n")
    for msg in conversation:
        file.write(f"{msg['role']}: {msg['content']}\n\n")
print("Conversation Saved!")


