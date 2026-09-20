from pathlib import Path

def load_markdown(path: str) -> str:
    file_path = Path(path)
    if file_path.suffix.lower == ".md":
        raise ValueError("Only Markdown files are allowed")

    return file_path.read_text(encoding="utf-8")

