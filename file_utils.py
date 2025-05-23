import os
import uuid
from typing import Tuple

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_TYPES = [
    "image/jpeg", "image/png",
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
]
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def save_file(file: bytes, filename: str, content_type: str) -> Tuple[str, str]:
    if content_type not in ALLOWED_TYPES:
        raise ValueError("Unsupported file type")
    if len(file) > MAX_FILE_SIZE:
        raise ValueError("File too large")

    unique_filename = f"{uuid.uuid4()}_{filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(file_path, "wb") as f:
        f.write(file)

    return unique_filename, file_path
