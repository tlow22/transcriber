from .base import TranscriptionService

# Utility for service registration/discovery (to be implemented)
_services = {}

def register_service(name: str, service_cls):
    _services[name] = service_cls

def get_service(name: str):
    return _services.get(name) 