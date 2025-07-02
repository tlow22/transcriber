import tempfile
import subprocess
import os
from typing import Optional


def download_audio_from_url(url: str, output_dir: Optional[str] = None) -> str:
    """
    Downloads audio from the given URL using yt-dlp in audio-only mode.
    Saves to a temporary file (or output_dir if provided) and returns the file path.
    """
    if output_dir is None:
        temp_dir = tempfile.TemporaryDirectory()
        output_dir = temp_dir.name
    else:
        os.makedirs(output_dir, exist_ok=True)
        temp_dir = None

    output_template = os.path.join(output_dir, '%(title)s.%(ext)s')
    cmd = [
        'yt-dlp',
        '-f', 'bestaudio/best',
        '--extract-audio',
        '--audio-format', 'mp3',
        '--output', output_template,
        url
    ]
    subprocess.run(cmd, check=True)

    # Find the downloaded file (should be the only file in output_dir)
    files = [f for f in os.listdir(output_dir) if f.endswith('.mp3')]
    if not files:
        raise RuntimeError('Audio download failed or no mp3 file found.')
    file_path = os.path.join(output_dir, files[0])

    # If using a temp dir, keep it alive by attaching to the file_path
    if temp_dir is not None:
        file_path = tempfile.NamedTemporaryFile(delete=False, dir=output_dir, suffix='.mp3').name

    return file_path 