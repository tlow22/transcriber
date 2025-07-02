import tempfile
import os
from typing import Dict
from downloader import download_audio_from_url
from . import get_service


def transcribe_url(url: str, service: str = "whisper") -> Dict:
    """
    Download audio from the given URL and transcribe it using the selected service.
    Args:
        url: The URL to download audio from.
        service: The transcription service to use (default: 'whisper').
    Returns:
        dict: Transcription result in the standard JSON schema.
    """
    temp_dir = tempfile.TemporaryDirectory()
    try:
        audio_path = download_audio_from_url(url, output_dir=temp_dir.name)
        service_cls = get_service(service)
        if service_cls is None:
            raise ValueError(f"Transcription service '{service}' not found.")
        transcriber = service_cls()
        result = transcriber.transcribe(audio_path)
        return result
    finally:
        temp_dir.cleanup() 