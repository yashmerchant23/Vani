from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

# generate speech by cloning a voice using default settings
tts.tts_to_file(text="Mom give me Tea and some snacks",
                file_path="output.wav",
                speaker_wav=["optimus prime 2.mp3"],
                language="en",
                split_sentences=True
                )

