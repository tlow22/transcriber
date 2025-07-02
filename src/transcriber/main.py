import tempfile
import os
from typing import Dict, Optional
from downloader import download_audio_from_url
from . import get_service


def transcribe_url(
    url: str,
    service: str = "whisper",
    audio_format: str = None,
    quality: str = None,
    keep_file: bool = False,
    temp_dir: Optional[str] = None,
    model_name: str = None,
    language: str = None
) -> Dict:
    """
    Download audio from the given URL and transcribe it using the selected service.
    Args:
        url: The URL to download audio from.
        service: The transcription service to use (default: 'whisper').
        audio_format: Audio format to extract (default: 'mp3' or $AUDIO_FORMAT).
        quality: Download quality (default: 'bestaudio/best' or $AUDIO_QUALITY).
        keep_file: If True, do not delete the file after use.
        temp_dir: Directory for temp files (default: system temp or $TEMP_DIR).
        model_name: Whisper model (default: 'base' or $WHISPER_MODEL).
        language: Language code hint for transcription (default: None or $LANGUAGE_HINT).
    Returns:
        dict: Transcription result in the standard JSON schema.
    """
    audio_format = audio_format or os.environ.get("AUDIO_FORMAT", "mp3")
    quality = quality or os.environ.get("AUDIO_QUALITY", "bestaudio/best")
    temp_dir = temp_dir or os.environ.get("TEMP_DIR")
    model_name = model_name or os.environ.get("WHISPER_MODEL", "base")
    language = language or os.environ.get("LANGUAGE_HINT")

    if temp_dir is None:
        temp_dir_obj = tempfile.TemporaryDirectory()
        temp_dir_path = temp_dir_obj.name
    else:
        os.makedirs(temp_dir, exist_ok=True)
        temp_dir_obj = None
        temp_dir_path = temp_dir

    try:
        audio_path = download_audio_from_url(
            url,
            output_dir=temp_dir_path,
            audio_format=audio_format,
            quality=quality,
            keep_file=keep_file
        )
        service_cls = get_service(service)
        if service_cls is None:
            raise ValueError(f"Transcription service '{service}' not found.")
        if service == "whisper":
            transcriber = service_cls(model_name=model_name)
            result = transcriber.transcribe(audio_path, language=language)
        else:
            transcriber = service_cls()
            result = transcriber.transcribe(audio_path)
        return result
    finally:
        if not keep_file and temp_dir_obj is not None:
            temp_dir_obj.cleanup() 