from . import TranscriptionService, register_service
from typing import Dict, Any
import whisper
import os

class WhisperTranscriptionService(TranscriptionService):
    def __init__(self, model_name: str = "base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path: str) -> Dict[str, Any]:
        result = self.model.transcribe(audio_path)
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