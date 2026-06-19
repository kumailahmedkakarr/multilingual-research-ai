# test_groq.py

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

print("API KEY =", os.getenv("GROQ_API_KEY"))

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Say hello"
        }
    ]
)

print(response.choices[0].message.content)