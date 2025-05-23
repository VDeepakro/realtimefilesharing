# 📁 Real-Time File Sharing App

A real-time file sharing system built with **FastAPI** and **WebSockets**.  
Users can upload files from their browser, and all connected users will instantly see new file uploads with metadata like username and timestamp.

---

## Features

- Real-time file broadcast using WebSockets
- Upload support for:
  - `.jpg`, `.png` images
  - `.pdf` documents
  - `.docx` Word files
- File size limit: **5MB**
- Upload metadata: filename, timestamp, sender's username
- Minimal, user-friendly web interface (HTML only, no frameworks)
- Files are stored in a local `uploads/` directory

---

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- HTML5 (Vanilla)
- Python 3.8+

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/VDeepakro/realtimefileshare.git
cd realtimefileshare



realtimefileshare/
│
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI app + WebSocket endpoint
│   ├── websocket_manager.py  # Handles WebSocket connections
│   ├── file_utils.py         # File saving, size/type checks
│   └── static/
│       └── index.html        # Web frontend
│
├── uploads/                  # Uploaded files are stored here
├── requirements.txt
└── README.md
```
