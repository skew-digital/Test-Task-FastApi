# Customer Message Processing API

A simple FastAPI app that classifies customer messages using OpenAI.

## What it does

Takes customer messages and automatically categorizes them as:

- Bug reports
- Feature requests
- General inquiries

## Setup

1. Install dependencies:

   ```bash
   pip install fastapi uvicorn openai python-dotenv pydantic
   ```

2. Create virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   .\venv\Scripts\activate   # On Windows
   ```

3. Create `.env` file:
   ```
   OPENAI_API_KEY=your_key_here
   ```

4. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```
View docs at: `http://localhost:8000/docs`

## Files

- `app/main.py` - API endpoint
- `app/services/classify.py` - OpenAI integration
- `app/services/processor.py` - Message processing
- `app/models/schemas.py` - Data models
