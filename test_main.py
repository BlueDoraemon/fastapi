from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app, get_video_id, get_transcript

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

def test_get_video_id():
    assert get_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == "dQw4w9WgXcQ"
    assert get_video_id("https://youtu.be/dQw4w9WgXcQ") == "dQw4w9WgXcQ"

def test_get_video_id_invalid():
    try:
        get_video_id("https://www.youtube.com/watch")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

@patch('main.YouTubeTranscriptApi.get_transcript')
def test_get_transcript(mock_get_transcript):
    mock_get_transcript.return_value = [{"text": "Hello"}, {"text": "World"}]
    assert get_transcript("dQw4w9WgXcQ") == "Hello World"

@patch('main.get_video_id')
@patch('main.get_transcript')
@patch('main.client.chat.completions.create')
def test_summarize_video(mock_create, mock_get_transcript, mock_get_video_id):
    mock_get_video_id.return_value = "dQw4w9WgXcQ"
    mock_get_transcript.return_value = "Sample transcript"
    mock_create.return_value = MagicMock(choices=[MagicMock(message=MagicMock(content="Summary"))])

    response = client.post("/summarize", json={"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"})
    assert response.status_code == 200
    assert response.json() == {"summary": "Summary"}

def test_summarize_video_invalid_url():
    response = client.post("/summarize", json={"url": "https://www.youtube.com/watch"})
    assert response.status_code == 500
    assert "Error summarizing video" in response.json()["detail"]
