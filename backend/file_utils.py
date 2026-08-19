from pathlib import Path
from dataclasses import dataclass

@dataclass
class FileMetadata:
    name: str
    size: int
    extension: str
    stem: str

SUPPORTED_EXTENSIONS = {".txt", ".pdf", ".docx", ".csv"}

def inspect_file(filename: str) -> FileMetadata:
    file_path = Path(filename)
    if file_path.exists():
        name = file_path.name
        extension = file_path.suffix
        stem = file_path.stem
        if extension not in SUPPORTED_EXTENSIONS:
            return {"error": f"Unsupported file extension: {extension}"}
        try:
            size = file_path.stat().st_size
        except OSError as e:
            return {"error": f"Could not retrieve file size: {e}"}
        return FileMetadata(
            name=name,
            size=size,
            extension=extension,
            stem=stem
        )
    else:
        return {"error": "File does not exist."}