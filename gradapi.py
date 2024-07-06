import requests

# Define the Gradio Space URL and the API endpoint
gradio_space_url = "https://huggingface.co/spaces/styletts2/styletts2"
api_endpoint = f"{gradio_space_url}/api/predict/"

# Define the input text and reference voice file path
text = "Dhoni finishes off in style. A magnificent strike into the crowd! India lift the World Cup after 28 years"
reference_voice_path = "Voices/AMitabh_Bachchanshort.wav"

# Prepare the payload
with open(reference_voice_path, "rb") as f:
    reference_voice_data = f.read()

payload = {
    "data": [text, reference_voice_data]
}

# Send a POST request to the API
response = requests.post(api_endpoint, files=payload)

# Check the response status
if response.status_code == 200:
    result = response.json()
    audio_url = result['data'][0]  # Assuming the response contains a URL to the generated audio
    
    # Download the generated audio file
    audio_response = requests.get(audio_url)
    with open("output_audio.wav", "wb") as f:
        f.write(audio_response.content)
    
    print(f"Audio file saved as 'output_audio.wav'")
else:
    print(f"Request failed with status code: {response.status_code}")