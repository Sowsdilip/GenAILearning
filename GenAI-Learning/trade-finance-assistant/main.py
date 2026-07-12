from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

print("API Key exists:", os.getenv("API_KEY") is not None)
print("Model:", os.getenv("MODEL"))

client = OpenAI(api_key = os.getenv("API_KEY"),
                base_url = "https://openrouter.ai/api/v1")

question = input("How can I help you today ?")

response = client.chat.completions.create(
    model = os.getenv("MODEL"),
    messages = [
        {
            "role" : "user",
            "content" : question
        }
    ]
)

print("\nAI Response:")
print(response.choices[0].message.content)