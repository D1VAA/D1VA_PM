from pathlib import Path

def get_actual_path() -> Path:
    return Path.cwd()