import requests

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio_data = request.files['audio'].read()  # assuming audio is sent as a file in the request (can be changed)
    url = 'https://whisper.lablab.ai/asr'
    files = {
        'audio_file': ('audio.wav', audio_data, 'audio/wav')
    }
    params = {
        'task': 'transcribe'
    }
    headers = {
        'Authorization': f'Bearer {whisper_api_key}'  # replace whisper_api_key with our actual API key
    }
    response = requests.post(url, files=files, params=params, headers=headers)
    transcription = response.json().get('text')
    return {'transcription': transcription}
