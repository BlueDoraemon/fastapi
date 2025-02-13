# README

## **YouTube Video Summarizer API**

This project is a FastAPI-based web application that extracts transcripts from YouTube videos and generates summaries using OpenAI's OpenRouter API. It is designed to process YouTube video URLs, fetch their transcripts, and return concise summaries.

---

## **Features**
- Extracts transcripts from YouTube videos using the `youtube-transcript-api`.
- Summarizes video content using OpenAI's language models via the OpenRouter API.
- Provides a RESTful API with endpoints for summarization and basic health checks.

---

## **Requirements**
- Python 3.9 or higher
- Dependencies listed in `requirements.txt`

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the project root directory and add the following variables:
     ```env
     OPENROUTER_API_KEY=<your_openrouter_api_key>
     YOUR_SITE_URL=<your_site_url>
     YOUR_SITE_NAME=<your_site_name>
     MODEL=<openai_model_name>  # e.g., gpt-4 or gpt-3.5-turbo
     ```

---

## **Usage**

### **Run the Application**
Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

### **Endpoints**

#### 1. **Summarize Video**
- **URL**: `/summarize`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "url": "https://www.youtube.com/watch?v=<video_id>"
  }
  ```
- **Response**:
  ```json
  {
    "summary": "<summarized_text>"
  }
  ```

#### 2. **Root Endpoint**
- **URL**: `/`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "greeting": "Hello, World!",
    "message": "Welcome to FastAPI!"
  }
  ```

---

## **How It Works**

1. The user sends a YouTube video URL to the `/summarize` endpoint.
2. The app extracts the video ID from the URL.
3. The transcript is fetched using the `youtube-transcript-api`.
4. The transcript is sent to OpenRouter's API for summarization.
5. A concise summary is returned to the user.

---

## **Error Handling**
- Handles invalid YouTube URLs with appropriate error messages.
- Catches exceptions during transcript fetching or summarization and returns meaningful HTTP error codes.

---

## **Dependencies**
Key dependencies include:
- `FastAPI`: For building the web API.
- `Pydantic`: For request and response validation.
- `youtube-transcript-api`: For fetching YouTube video transcripts.
- `openai`: For interacting with OpenRouter's API.
- `python-dotenv`: For managing environment variables.

---

## **Future Improvements**
- Add support for multilingual transcripts and summaries.
- Implement caching for frequently summarized videos.
- Enhance error handling for unsupported videos (e.g., no captions).

---
