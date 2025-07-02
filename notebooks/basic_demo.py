# %% [markdown]
"""
# Transcriber: Basic Marimo Demo

This notebook demonstrates how to use the transcriber package to download and transcribe audio from a URL (e.g., YouTube) using Whisper.
"""

# %% [markdown]
"""
## Installation

If you haven't already, install the package and dependencies:
```sh
uv pip install -e .
uv pip install yt-dlp openai-whisper marimo
```
"""

# %%
from transcriber.main import transcribe_url

# %% [markdown]
"""
## Transcribe from a YouTube URL
Enter a YouTube (or other supported) URL below. The transcription will use the default Whisper model (base).
"""

# %%
import marimo as mo
url = mo.ui.text(label="YouTube or audio URL", value="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
url

# %%
if url.value:
    result = transcribe_url(url.value)
    result
else:
    print("Please enter a URL above.")

# %% [markdown]
"""
## Output Explanation
- `text`: The full transcription as a string.
- `segments`: List of segments with start/end times and text.
- `language`: Detected language code.
"""

# %% [markdown]
"""
## Advanced Usage: Configuration
You can customize the transcription process with additional options:

- `model_name`: Whisper model ("tiny", "base", "small", "medium", "large")
- `audio_format`: Output audio format (e.g., "mp3", "wav")
- `quality`: Download quality (e.g., "bestaudio/best")
- `language`: Language code hint (e.g., "en")

Example:
```python
result = transcribe_url(
    url.value,
    model_name="small",
    audio_format="wav",
    quality="bestaudio/best",
    language="en"
)
```
""" 