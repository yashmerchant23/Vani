
from transformers import AutoTokenizer, AutoModelForCausalLM
import warnings 

warnings.simplefilter(action = 'ignore' , category =FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

# Define the Hugging Face model path
hf_path = 'jiajunlong/TinyLLaVA-OpenELM-450M-CLIP-0.55B'

# Load the model
model = AutoModelForCausalLM.from_pretrained(hf_path, trust_remote_code=True)
config = model.config

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(hf_path, use_fast=False, model_max_length=config.max_length)

# Define prompt and image URL
prompt = "Describe the image. descriptions should be concise yet vivid, highlighting any notable features or behaviors. Try to keep it lighthearted and entertaining, but avoid repeating yourself. Remember to point out anything particularly interesting!"
image_url = "frames/frame.jpg"

# Truncate the prompt if it exceeds the maximum length
truncated_prompt = prompt[:config.max_length]

# Enable sampling if using temperature
model.config.do_sample = True  # Enable sampling
model.config.temperature = 1.0  # Set temperature (adjust as needed)

# Generate text based on prompt and image
output_text, generation_time = model.chat(prompt=truncated_prompt, image=image_url, tokenizer=tokenizer)


# Clean and print the output
cleaned_output_text = output_text.replace('\n', ' ').strip()
print('Cleaned model output:', cleaned_output_text)
print('Running time:', generation_time)

