
# from gradio_client import Client

# client = Client("abidlabs/en2fr")
# job = client.submit("Hello.", api_name="/predict")  # This is not blocking

# # Do something else

# print(job.result())  # This is blocking

import requests
from gradio_client import Client
import time

# Define the client
client = Client("https://coqui-xtts.hf.space/")

# Define the input parameters
text_prompt = "Hello, this is a test text to speech conversion."
language = "en,en"
reference_audio_url = "Voices/AMitabh_Bachchan.wav"

# Retry mechanism
max_retries = 3
attempt = 0
timeout = 60  # seconds

while attempt < max_retries:
    try:
        # Start the timer
        start_time = time.time()

        # Make the API call
        response = client.predict(
            text_prompt,  # str  in 'Text Prompt' Textbox component
            language,     # str in 'Language' Dropdown component
            reference_audio_url,  # str (URL or filepath) in 'Reference Audio' Audio component
            reference_audio_url,  # str (URL or filepath) in 'Use Microphone for Reference' Audio component
            True,  # bool in 'Use Microphone' Checkbox component
            True,  # bool in 'Cleanup Reference Voice' Checkbox component
            True,  # bool in 'Do not use language auto-detect' Checkbox component
            True,  # bool in 'Agree' Checkbox component
            fn_index=1
        )

        # End the timer
        end_time = time.time()

        # Check if the request took longer than the timeout
        if end_time - start_time > timeout:
            raise requests.exceptions.Timeout("The request timed out.")

        # Check the response status code
        if response.status_code == 200:
            # Parse the response JSON
            result = response.json()
            synthesized_audio_url = result.get("synthesized_audio_url")
            if synthesized_audio_url:
                # Download the audio file
                audio_response = requests.get(synthesized_audio_url)
                with open("synthesized_audio.wav", "wb") as audio_file:
                    audio_file.write(audio_response.content)
                print("Audio file downloaded as 'synthesized_audio.wav'")
                break  # Exit the loop if successful
            else:
                print("Synthesized audio URL not found in the response.")
        else:
            print(f"API request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        attempt += 1
        print(f"Attempt {attempt} failed: {e}")
        if attempt == max_retries:
            print("Max retries reached. Exiting.")
            break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        break