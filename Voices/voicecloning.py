

from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

# generate speech by cloning a voice using default settings
tts.tts_to_file(text="I am king khan. the badshah of bollywood and the owner of Mannat",
                file_path="output.wav",
                speaker_wav=["obama_30_sec.wav"],
                language="en",
                split_sentences=True
                )

