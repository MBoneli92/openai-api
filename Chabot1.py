import openai
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("The API key was not found in .env.")

client = openai.OpenAI(api_key=api_key)

def generate_reply(messages, model="gpt-3.5-turbo", max_tokens=1000, temperature=0):
    response_stream = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=messages,
        stream=True  # Streaming response
    )

    full_response = ""
    print("🤖 Assistant:", end=" ", flush=True)

    for chunk in response_stream:
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
            full_response += content

    print()  # Line break
    return full_response

# Start conversation
conversation = []

print("💬 ChatGPT Terminal Chatbot (type 'exit' to quit)\n")

while True:
    try:
        # Get user input
        user_input = input("👤 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        # Append user message
        conversation.append({"role": "user", "content": user_input})

        # Get assistant reply
        assistant_reply = generate_reply(conversation)

        # Append assistant message
        conversation.append({"role": "assistant", "content": assistant_reply})

    except KeyboardInterrupt:
        print("\n👋 Interrupted. Exiting chat.")
        break
    except Exception as e:
        print(f"\n⚠️ Error: {e}")
        break
