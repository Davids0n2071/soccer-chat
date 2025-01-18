from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class UserQuestion(BaseModel):
    question: str

app = FastAPI()
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)

@app.post("/chat-with-ai")
async def chat_with_ai(user_question: UserQuestion):
    try:
        # Generate a completion using the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-2024-11-20",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"You are a helpful assistant that only answers questions about soccer. If the question is unrelated to soccer, politely respond that you can only answer soccer-related questions. This is the question {user_question}"
                        },
                    ]
                }
            ],
            max_tokens=300
        )

        # Procesar la respuesta de OpenAI
        result = response.choices[0].message.content

        print(f"result {result}")

        return {
            "success": True,
            "response": result
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
