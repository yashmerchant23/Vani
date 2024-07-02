# from transformers import AutoTokenizer, AutoModelForCausalLM

# # Define the Hugging Face model path
# hf_path = 'jiajunlong/TinyLLaVA-OpenELM-450M-SigLIP-0.89B'

# # Load the model
# model = AutoModelForCausalLM.from_pretrained(hf_path, trust_remote_code=True)
# config = model.config

# # Load the tokenizer
# tokenizer = AutoTokenizer.from_pretrained(hf_path, use_fast=False, model_max_length=config.max_length)

# # Define prompt and image URL
# prompt = "describe the image?"
# image_url = "face.jpg"

# # Generate text based on prompt and image
# output_text, generation_time = model.chat(prompt=prompt, image=image_url, tokenizer=tokenizer)

# # Print outputs
# print('Model output:', output_text)
# print('Running time:', generation_time)


from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import torch.quantization

# Define the Hugging Face model path
hf_path = 'jiajunlong/TinyLLaVA-OpenELM-450M-SigLIP-0.89B'

# Load the model
model = AutoModelForCausalLM.from_pretrained(hf_path, trust_remote_code=True)
config = model.config

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(hf_path, use_fast=True, model_max_length=config.max_length)

# Add quantization and dequantization modules to the model
model.quant = torch.quantization.QuantStub()
model.dequant = torch.quantization.DeQuantStub()

# Convert the model to a quantized version
model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)

# Define prompt and image URL
prompt = "describe the image?"
image_url = "face.jpg"

# Prepare inputs for the model
inputs = tokenizer(prompt, return_tensors="pt")

# Perform inference
with torch.no_grad():
    outputs = model.generate(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'])

# Decode the generated sequence
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Print model output
print('Model output:', generated_text)


