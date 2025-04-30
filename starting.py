import openai
from dotenv import load_dotenv
import os

load_dotenv() # Carrega as variáveis do arquivo .env

api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("the API key was not found in .env.")

client = openai.OpenAI(api_key=api_key)

def generate_reply(messages, model="gpt-3.5-turbo", max_tokens=1000, temperature=0):
    response_stream = client.chat.completions.create(
    model=model,
    max_tokens=max_tokens,
    temperature=temperature,
    messages=messages,
    stream=True ##Prints the text word per word
    )
    full_response = ""
    print("🤖 Assistant:", end=" ", flush=True)

    for chunk in response_stream:
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
            full_response += content

    print()  # New line after stream ends
    return full_response

# Start conversation
conversation = []

# First user message
user_input_1 = "Describe an apple in 5 words"
conversation.append({"role": "user", "content": user_input_1})
print("👤 User:", user_input_1)

# Assistant response
assistant_reply_1 = generate_reply(conversation)
conversation.append({"role": "assistant", "content": assistant_reply_1})
print("🤖 Assistant:", assistant_reply_1)

# Second user message
user_input_2 = "Now describe a banana in 5 words"
conversation.append({"role": "user", "content": user_input_2})
print("👤 User:", user_input_2)

# Assistant response
assistant_reply_2 = generate_reply(conversation)
conversation.append({"role": "assistant", "content": assistant_reply_2})
print("🤖 Assistant:", assistant_reply_2)

# conversation = [
#     {"role": "user", "content": "Describe an apple in 5 words"},
# ]
# # Print the response
# reply = generate_reply(conversation)
# print("✅ Connection successful!")
# print("User: ", conversation)
# print("OpenAI says:", reply)

# ##Continue conversation
# conversation.append({"role": "assistant", "content": reply})
# conversation.append({"role": "user", "content": "Now describe a banana in 5 words"})

# reply2 = generate_reply(conversation)
# print("OpenAI says:", reply2)