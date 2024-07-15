from transformers import AutoTokenizer, AutoModelForCausalLM
import time
import os
import cv2
import warnings
import sounddevice as sd
import soundfile as sf
from TTS.api import TTS

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

# Define the Hugging Face model path
hf_path = 'jiajunlong/TinyLLaVA-OpenELM-450M-SigLIP-0.89B'

# Load the model
model = AutoModelForCausalLM.from_pretrained(hf_path, trust_remote_code=True)
config = model.config

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(hf_path, use_fast=False)

# Define prompt and image path
prompt = ("Imagine you are narrating a Discovery Channel documentary about this image. Describe it with scientific accuracy, but don’t hesitate to inject some humor. Be witty and sarcastic while ensuring your facts are spot-on. Avoid repeating any statements, and keep the audience engaged with your clever observations.")
image_path = "../frames/frame.jpg"

# Increase the prompt size buffer
max_prompt_length = 1000
truncated_prompt = prompt[:max_prompt_length]

# Initialize TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

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

                # Clean the output
                cleaned_output_text = output_text.replace('\n', ' ').strip()

                # Print the generated text
                print(cleaned_output_text)

                # Use the generated text for voice cloning
                tts.tts_to_file(
                    text=cleaned_output_text,
                    file_path="output.wav",
                    speaker_wav=["optimus prime 2.mp3"],
                    language="en",
                    split_sentences=True
                )

                # Play the generated audio
                data, fs = sf.read("output.wav", dtype='float32')
                sd.play(data, fs)
                sd.wait()

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
