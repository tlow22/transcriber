from . import TranscriptionService, register_service
from typing import Dict, Any, Optional
import whisper
import os

class WhisperTranscriptionService(TranscriptionService):
    def __init__(self, model_name: str = "base"):
        self.model_name = model_name
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path: str, language: Optional[str] = None) -> Dict[str, Any]:
        """
        Transcribe the given audio file using Whisper.
        Args:
            audio_path: Path to the audio file.
            language: Optional language code hint (e.g., 'en').
        Returns:
            dict: Transcription result in the standard JSON schema.
        """
        result = self.model.transcribe(audio_path, language=language)
        # result: { 'text': ..., 'segments': [...], 'language': ... }
        # segments: list of { 'id', 'seek', 'start', 'end', 'text', ... }
        segments = [
            {"start": s["start"], "end": s["end"], "text": s["text"]}
            for s in result.get("segments", [])
        ]
        return {
            "text": result.get("text", ""),
            "segments": segments,
            "language": result.get("language", "")
        }

# Register the service
register_service("whisper", WhisperTranscriptionService) 