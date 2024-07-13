from transformers import AutoTokenizer, AutoModelForCausalLM
import time
import os
import cv2
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

# Define the Hugging Face model path
hf_path = 'jiajunlong/TinyLLaVA-OpenELM-450M-CLIP-0.55B'

# Load the model
model = AutoModelForCausalLM.from_pretrained(hf_path, trust_remote_code=True)
config = model.config

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(hf_path, use_fast=False)

# Define prompt and image path
prompt = "Imagine you are narrating a Discovery Channel documentary about this image. Describe it with scientific accuracy, but don’t hesitate to inject some humor. Be witty and sarcastic while ensuring your facts are spot-on. Avoid repeating any statements, and keep the audience engaged with your clever observations."
image_path = "disco.jfif"

# Increase the prompt size buffer (for example, set to 512 characters)
max_prompt_length = 1000
truncated_prompt = prompt[:max_prompt_length]

# Function to read the latest image and generate text
def generate_text_for_latest_image():
    while True:
        try:
            # Check if the image file exists
            if os.path.exists(image_path):
                # Load the image
                frame = cv2.imread(image_path)

                # Generate text based on the image
                output_text, generation_time = model.chat(prompt=truncated_prompt, image=image_path, tokenizer=tokenizer)

                # Clean and print the output
                cleaned_output_text = output_text.replace('\n', ' ').strip()
                print('Cleaned model output:', cleaned_output_text)
                print('Running time:', generation_time)

                # Sleep for a moment before generating text again
                time.sleep(1)
        
        except KeyboardInterrupt:
            print("Stopping the script...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(5)

# Run the function to continuously generate text for the latest image
generate_text_for_latest_image()

# Clean up
cv2.destroyAllWindows()
