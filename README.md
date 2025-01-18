# Soccer Chat Bot 🤖⚽

A FastAPI-based REST API that provides soccer-related information using OpenAI's GPT-4 model. This bot is specifically designed to answer questions about soccer/football and politely deflects non-soccer related queries.

## Features

- REST API endpoint for soccer-related questions
- Powered by OpenAI's GPT-4 model
- Input validation using Pydantic
- Error handling and meaningful responses
- Environment variable configuration

## Prerequisites

- Python 3.12 or higher
- OpenAI API key
- The dependencies listed in requirements.txt

## Installation

1. Clone the repository:
bash
git clone https://github.com/Davids0n2071/soccer-chat.git
cd soccer-chat


2. Create a virtual environment and activate it:
bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate


3. Install the required dependencies:
bash
pip install -r requirements.txt


4. Create a .env file in the root directory and add your OpenAI API key:
bash
OPENAI_API_KEY=your_api_key_here


## Usage

1. Start the server:
bash
python main.py


The server will start on http://0.0.0.0:8080

2. Send requests to the API:

bash
curl -X POST "http://localhost:8080/items" \
     -H "Content-Type: application/json" \
     -d '{"question": "Who won the 2022 FIFA World Cup?"}'


### API Endpoints

#### POST /items

Accepts a JSON payload with a question and returns soccer-related information.

Request body:
json
{
    "question": "string"
}


Success Response:
json
{
    "success": true,
    "response": "string"
}


Error Response:
json
{
    "success": false,
    "error": "error message"
}


## Example Queries

bash
# Valid soccer-related question
curl -X POST "http://localhost:8080/chat-with-ai" \
     -H "Content-Type: application/json" \
     -d '{"question": "Who is Lionel Messi?"}'

# Non-soccer question (will receive a polite deflection)
curl -X POST "http://localhost:8080/chat-with-ai" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is the capital of France?"}'


## Project Structure

The main application code can be found in main.py, which contains:
- FastAPI application setup
- OpenAI client configuration
- Request handling and response processing
- Error handling

Reference to main application code:
python:main.py
startLine: 1
endLine: 58


## Dependencies

Key dependencies include:
- FastAPI (v0.115.6)
- OpenAI (v1.59.8)
- Pydantic (v2.10.5)
- Python-dotenv (v1.0.1)
- Uvicorn (v0.34.0)

For a complete list of dependencies, see:
requirements.txt
startLine: 1
endLine: 22


## Error Handling

The application includes robust error handling:
- Validates the presence of OpenAI API key
- Handles API request failures
- Returns meaningful error messages in the response

## Environment Variables

Required environment variables:
- OPENAI_API_KEY: Your OpenAI API key
