"""
Pytest test cases for the AI Study Assistant API.
- Test 1: Valid question with mocked LLM response.
- Test 2: Invalid input (empty question) returns 422.
- Test 3: Missing question field returns 422.
- Test 4: Root endpoint health check.
"""

from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_ask_valid_question():
    """Test that a valid question returns a 200 response with the expected answer."""
    mock_answer = "Machine learning is a subset of AI that enables systems to learn from data."

    with patch("main.get_llm_response", return_value=mock_answer):
        response = client.post("/ask", json={"question": "What is machine learning?"})

    assert response.status_code == 200
    data = response.json()
    assert data["question"] == "What is machine learning?"
    assert data["answer"] == mock_answer


def test_ask_empty_question():
    """Test that an empty question string returns a 422 validation error."""
    response = client.post("/ask", json={"question": ""})

    assert response.status_code == 422


def test_ask_missing_question_field():
    """Test that a request missing the 'question' field returns a 422 error."""
    response = client.post("/ask", json={})

    assert response.status_code == 422


def test_root_endpoint():
    """Test the health-check root endpoint."""
    response = client.get("/")

    assert response.status_code == 200
    assert "AI Study Assistant API is running" in response.json()["message"]
