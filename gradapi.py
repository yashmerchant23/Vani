
# from gradio_client import Client

# client = Client("abidlabs/en2fr")
# job = client.submit("Hello.", api_name="/predict")  # This is not blocking

# # Do something else

# print(job.result())  # This is blocking

from gradio_client import Client, handle_file

client = Client("CAMB-AI/mars5_space")
result = client.predict(
		text="Hello!!",
		audio_file=handle_file('Voices/trump_30_sec.wav'),
		prompt_text="Hello!!",
		temperature=0.8,
		top_k=-1,
		top_p=0.2,
		typical_p=1,
		freq_penalty=2.6,
		presence_penalty=0.4,
		rep_penalty_window=100,
		nar_guidance_w=3,
		deep_clone=True,
		api_name="/on_click"
)
print(result)