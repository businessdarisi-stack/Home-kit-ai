from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import openai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask(question: Question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question.question,
        max_tokens=150
    )
    return {"answer": response.choices[0].text.strip()}
