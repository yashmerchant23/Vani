from transformers import AutoTokenizer, AutoModelForCausalLM

# Define the Hugging Face model path
hf_path = 'jiajunlong/TinyLLaVA-OpenELM-450M-SigLIP-0.89B'

# Load the model
model = AutoModelForCausalLM.from_pretrained(hf_path, trust_remote_code=True)
config = model.config

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(hf_path, use_fast=False, model_max_length=config.max_length)

# Define prompt and image URL
prompt = "Describe the image. descriptions should be concise yet vivid, highlighting any notable features or behaviors. Try to keep it lighthearted and entertaining, but avoid repeating yourself. Remember to point out anything particularly interesting!"
image_url = "soccer_practice.jpg"

# Generate text based on prompt and image
output_text, generation_time = model.chat(prompt=prompt, image=image_url, tokenizer=tokenizer)

# Print outputs
print('Model output:', output_text)
print('Running time:', generation_time)







