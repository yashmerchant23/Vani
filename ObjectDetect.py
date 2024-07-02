from PIL import Image
import requests
from io import BytesIO
from transformers import pipeline

# initialize the image-to-text model
prompt = """You are Sir David Attenborough. Describe this photo as if it were part of a nature documentary. Be witty, humorous, and concise. Avoid repetition. If there's something unusual happening, emphasize it."""
model = pipeline("text-generation", model="llava-hf/llava-v1.6-mistral-7b-hf", tokenizer="llava-hf/llava-v1.6-mistral-7b-hf", configuration={"max_length": 50, "num_beams": 4, "early_stopping": True, "num_return_sequences": 1})

def image_to_text(image_path):
    # load the image
    image = Image.open(image_path).resize((224, 224))
    
    # convert the image to bytes
    byte_io = BytesIO()
    image.save(byte_io, format='JPEG')
    img_bytes = byte_io.getvalue()

    # send a request to the Hugging Face endpoint to generate text from the image
    response = requests.post(
        "https://api-inference.huggingface.co/models/llava-hf/llava-v1.6-mistral-7b-hf",
        headers={
            "Authorization": "Bearer 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",
            "Content-Type": "application/json",
        },
        json={
            "inputs": {"image": img_bytes},
            "parameters": {
                "return_tensors": False,
                "use_fast": True,
                "seed": 42,
            }
        },
    )
    result = response.json()[0]['generated_text'][len(prompt):]

    # return the generated text
    return result

# continuously convert the latest frame.jpg image to text
while True:
    image_path = "frames/frame.jpg"
    text = image_to_text(image_path)
    print(text)