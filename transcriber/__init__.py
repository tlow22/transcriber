import abc
from typing import Dict, Any

class TranscriptionService(abc.ABC):
    """
    Abstract base class for transcription services.
    Implementations must provide the transcribe method.
    """
    @abc.abstractmethod
    def transcribe(self, audio_path: str) -> Dict[str, Any]:
        """
        Transcribe the given audio file and return a JSON dict with:
        {
            "text": str,  # Full transcription
            "segments": list,  # List of {"start": float, "end": float, "text": str}
            "language": str  # Detected language code
        }
        """
        pass

# Utility for service registration/discovery (to be implemented)
_services = {}

def register_service(name: str, service_cls):
    _services[name] = service_cls

def get_service(name: str):
    return _services.get(name) 