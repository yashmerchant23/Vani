# import simpleaudio as sa
# from gradio_client import Client
# import httpx

# # Set the timeout for the client
# client = httpx.Client(timeout=httpx.Timeout(30.0))

# # Define the client
# client = Client("https://coqui-xtts.hf.space/--replicas/ldw7u/")

# # Define the input parameters
# text_prompt = "Create an emotional orchestral piece with a slow, haunting melody that conveys deep sorrow and farewell."
# language = "en,en"
# reference_audio_url = "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",


# # Query the API
# result = client.predict(
#     text_prompt,
#     language,
#     reference_audio_url,
#     reference_audio_url,
#     True,
#     True,
#     True,
#     True,  # Using the same URL for reference audio and microphone
#     fn_index=1
# )

# # Extract the URL of the synthesized audio
# synthesized_audio_url = result[1]

# # Play the generated audio
# import requests
# from tempfile import NamedTemporaryFile

# def play_audio_from_url(url):
#     # Download the audio file
#     response = requests.get(url)
#     temp_audio = NamedTemporaryFile(delete=False, suffix=".wav")
#     temp_audio.write(response.content)
#     temp_audio.close()
    
#     # Play the audio file
#     wave_obj = sa.WaveObject.from_wave_file(temp_audio.name)
#     play_obj = wave_obj.play()
#     play_obj.wait_done()

# # Play the synthesized audio
# play_audio_from_url(synthesized_audio_url)

# from gradio_client import Client

# client = Client("https://coqui-xtts.hf.space/--replicas/ldw7u/")
# result = client.predict(
# 		"Howdy!",	# str  in 'Text Prompt' Textbox component
# 		"en,en",	# str (Option from: [('en', 'en'), ('es', 'es'), ('fr', 'fr'), ('de', 'de'), ('it', 'it'), ('pt', 'pt'), ('pl', 'pl'), ('tr', 'tr'), ('ru', 'ru'), ('nl', 'nl'), ('cs', 'cs'), ('ar', 'ar'), ('zh-cn', 'zh-cn'), ('ja', 'ja'), ('ko', 'ko'), ('hu', 'hu'), ('hi', 'hi')]) in 'Language' Dropdown component
# 		"https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",	# str (filepath on your computer (or URL) of file) in 'Reference Audio' Audio component
# 		"https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",	# str (filepath on your computer (or URL) of file) in 'Use Microphone for Reference' Audio component
# 		True,	# bool  in 'Use Microphone' Checkbox component
# 		True,	# bool  in 'Cleanup Reference Voice' Checkbox component
# 		True,	# bool  in 'Do not use language auto-detect' Checkbox component
# 		True,	# bool  in 'Agree' Checkbox component
# 		fn_index=1
# )
# print(result).

from gradio_client import Client

client = Client("https://kaiosan-voice-cloning22.hf.space/--replicas/mm6jg/")

try:
    result = client.predict(
        "Test text",  # Simplified text input
        "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",  # Known good URL
        "en",  # Use English to simplify
        api_name="/predict"
    )
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")



