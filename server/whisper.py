import requests

API_URL = "https://whisper.lablab.ai"

def transcribe_audio(audio_file):
    url = f"{API_URL}/asr"
    files = {"audio_file": ("audio.wav", audio_file, "audio/wav")}
    response = requests.post(url, files=files)
    response.raise_for_status()
    return response.json()["text"]
