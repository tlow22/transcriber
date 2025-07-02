# /// script
# [tool.marimo.runtime]
# auto_instantiate = false
# ///

import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Transcriber: Basic Marimo Demo

    How to use the `transcriber package to download and transcribe audio-to-text. 
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Transcribe from a YouTube URL
    Enter a YouTube (or other supported) URL below. The transcription will use the default Whisper model (base).
    """
    )
    return


@app.cell
def _():
    youtube_embed = """<iframe width="642" height="1141" src="https://www.youtube.com/embed/iOZk8j4fp7U" title="The Best Guacamole Recipe" frameborder="3" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>"""
    return (youtube_embed,)


@app.cell
def _(mo, youtube_embed):
    mo.iframe(youtube_embed, width=800, height=800)
    return


@app.cell
def _(mo):
    url = mo.ui.text(label="YouTube or audio URL", value="https://www.youtube.com/shorts/iOZk8j4fp7U")
    url
    return (url,)


@app.cell
def _(mo, url):
    from transcriber.main import transcribe_url
    if url.value:
        result = transcribe_url(url.value)
        mo.display(result)
    else:
        mo.display("Please enter a URL above.")
    return


@app.cell
def _(mo):
    # Markdown: Output explanation
    mo.md("""
    ## Output Explanation
    - `text`: The full transcription as a string.
    - `segments`: List of segments with start/end times and text.
    - `language`: Detected language code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
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
    )
    return


if __name__ == "__main__":
    app.run()
