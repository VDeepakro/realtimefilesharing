from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .websocket_manager import manager
from .file_utils import save_file
from datetime import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/")
async def get():
    with open("app/static/index.html") as f:
        return HTMLResponse(f.read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            username = data["username"]
            filename = data["filename"]
            content_type = data["content_type"]
            file_data = bytes(data["file_data"])
            try:
                unique_filename, _ = save_file(file_data, filename, content_type)
                timestamp = datetime.utcnow().isoformat()
                file_url = f"/uploads/{unique_filename}"
                await manager.broadcast({
                    "username": username,
                    "filename": filename,
                    "timestamp": timestamp,
                    "file_url": file_url
                })
            except ValueError as e:
                await websocket.send_json({"error": str(e)})
    except WebSocketDisconnect:
        manager.disconnect(websocket)
