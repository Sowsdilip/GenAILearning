from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

print("API Key exists:", os.getenv("API_KEY") is not None)
print("Model:", os.getenv("MODEL"))

client = OpenAI(api_key = os.getenv("API_KEY"),
                base_url = "https://openrouter.ai/api/v1")

def ask_ai(question):
    
    response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        temperature = 0.5,
        messages = [
        {
            "role" : "user",
            "content" : question
        }
        ]
    )
    
    return response.choices[0].message.content

while True:
  question = input("How can I help you today ?")
  if question.lower() == "exit":
     print("good bye")
     break
  response = ask_ai(question)         

  print("\nAI Response:")
  print(response)