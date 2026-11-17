"""
AI Study Assistant API
Course: Machine Learning Operations (24SDAD03)
A FastAPI application that accepts a student's question and generates
an answer using OpenAI LLM.
"""

import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Configure the OpenAI client
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

app = FastAPI(
    title="AI Study Assistant API",
    description="An API that accepts a student's question and generates an answer using an LLM.",
    version="1.0.0",
)


class Question(BaseModel):
    """Request model for the /ask endpoint."""
    question: str

    @field_validator("question")
    @classmethod
    def question_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Question must not be empty")
        return v.strip()


class Answer(BaseModel):
    """Response model for the /ask endpoint."""
    question: str
    answer: str


def get_llm_response(question: str) -> str:
    """Connect to OpenAI LLM and generate an answer."""
    if not client:
        raise HTTPException(
            status_code=500,
            detail="OPENAI_API_KEY is not configured. Set it in the .env file.",
        )

    prompt = (
        "You are a helpful AI study assistant. A student has asked the "
        "following question. Provide a clear and concise answer.\n\n"
        f"Question: {question}"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=512,
    )
    return response.choices[0].message.content


@app.get("/")
def root():
    """Health check / root endpoint."""
    return {"message": "AI Study Assistant API is running. POST to /ask to ask a question."}


@app.post("/ask", response_model=Answer)
def ask_question(payload: Question):
    """
    Accept a student's question in JSON format and return an LLM-generated answer.

    **Request body:**
    ```json
    { "question": "What is machine learning?" }
    ```
    """
    answer_text = get_llm_response(payload.question)
    return Answer(question=payload.question, answer=answer_text)
