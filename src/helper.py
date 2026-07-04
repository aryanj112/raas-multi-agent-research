from pathlib import Path

import mediapy as media

VIDEOS_DIR = Path(__file__).resolve().parent.parent / "videos"


def save_video(frames, name, fps=30):
    VIDEOS_DIR.mkdir(exist_ok=True)
    path = VIDEOS_DIR / name
    media.write_video(path, frames, fps=fps)
    return path
