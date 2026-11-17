# AI Study Assistant API

A FastAPI application that accepts a student's question and generates an answer using OpenAI LLM.

**Course:** Machine Learning Operations (24SDAD03)  
**Date:** 17 November 2026  
**Course Coordinator:** Dr Sandeep Chitreddy

---

## Project Structure

```
├── main.py                        # FastAPI application
├── test_main.py                   # Pytest test cases
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker containerization
├── .env                           # API key configuration (not committed)
├── .gitignore                     # Git ignore rules
└── .github/
    └── workflows/
        └── test.yml               # GitHub Actions CI workflow
```

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/arnav-mishra28/MLOps_End-sem-1-.git
cd MLOps_End-sem-1-
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API key

Create a `.env` file and add your OpenAI API key:

```
OPENAI_API_KEY=your_actual_api_key_here
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Usage

### POST `/ask`

Send a JSON payload with a question:

```bash
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is machine learning?"}'
```

**Response:**

```json
{
  "question": "What is machine learning?",
  "answer": "Machine learning is a subset of artificial intelligence..."
}
```

### Interactive Docs

Visit `http://127.0.0.1:8000/docs` for the Swagger UI.

## Running Tests

```bash
pytest test_main.py -v
```

The tests mock the LLM response so no API key is needed.

## Docker

### Build the image

```bash
docker build -t study-assistant-api .
```

### Run the container

```bash
docker run -p 8000:8000 study-assistant-api
```

## GitHub Actions

The CI workflow (`.github/workflows/test.yml`) automatically runs all tests on every push and pull request.
