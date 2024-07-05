from transformers import pipeline
import sounddevice as sd
import soundfile as sf

# Load the espeak-ng-tts text-to-speech model
tts = pipeline("text-to-speech", model="espeak-ng-tts")

# Generate speech from text
text = "The quick brown fox jumps over the lazy dog."
audio = tts(text)

# Save the generated audio to a file
audio_data = audio["audio"]
sample_rate = audio["sample_rate"]
sf.write("output.wav", audio_data, sample_rate)

# Play the generated audio
sd.play(audio_data, sample_rate)
sd.wait()