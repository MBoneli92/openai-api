import openai
from dotenv import load_dotenv
import os

load_dotenv() # Carrega as variáveis do arquivo .env

api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("the API key was not found in .env.")

client = openai.OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Say hello!"}
    ]
)

# Print the response
print("✅ Connection successful!")
print("OpenAI says:", response.choices[0].message.content)