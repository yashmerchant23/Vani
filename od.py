from transformers import AutoTokenizer, AutoModelForCausalLM

# Define the Hugging Face model path
hf_path = 'jiajunlong/TinyLLaVA-OpenELM-450M-SigLIP-0.89B'

# Load the model
model = AutoModelForCausalLM.from_pretrained(hf_path, trust_remote_code=True)
config = model.config

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(hf_path, use_fast=False,
                                          model_max_length=config.max_position_embeddings)

# Define prompt and image URL
prompt = "describe the image?"
image_url = "./frames/frame.jpg"

# Generate text based on prompt and image
output_text, generation_time = model.chat(prompt=prompt, image=image_url, tokenizer=tokenizer)

# Print outputs
print('Model output:', output_text)
print('Running time:', generation_time)






