import simpleaudio as sa
from gradio_client import Client

# Define the client
client = Client("https://coqui-xtts.hf.space/--replicas/ldw7u/")

# Define the input parameters
text_prompt = "Create an emotional orchestral piece with a slow, haunting melody that conveys deep sorrow and farewell."
language = "en,en"
reference_audio_url = "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav"

# Query the API
result = client.predict(
    text_prompt,
    language,
    reference_audio_url,
    reference_audio_url,  # Using the same URL for reference audio and microphone
    fn_index=1
)

# Extract the URL of the synthesized audio
synthesized_audio_url = result[1]

# Play the generated audio
import requests
from tempfile import NamedTemporaryFile

def play_audio_from_url(url):
    # Download the audio file
    response = requests.get(url)
    temp_audio = NamedTemporaryFile(delete=False, suffix=".wav")
    temp_audio.write(response.content)
    temp_audio.close()
    
    # Play the audio file
    wave_obj = sa.WaveObject.from_wave_file(temp_audio.name)
    play_obj = wave_obj.play()
    play_obj.wait_done()

# Play the synthesized audio
play_audio_from_url(synthesized_audio_url)
