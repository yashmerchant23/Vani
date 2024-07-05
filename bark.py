from TTS.tts.configs.bark_config import BarkConfig
from TTS.tts.models.bark import Bark
from scipy.io.wavfile import wrtie as wite_wav

config = BarkConfig()
model = Bark.init_from_config(config)
model.load_checkpoint(config,checkpoint_dir ="bark/",eval=True)

text = "Dhoni finishes off in style. A magnificent strike into the crowd! India lift the World Cup after 28 years"


output_dict = model.synthesize(
    text,
    config,
    speaker_id ="speaker",
    voice_dirs ="bark_voices",
    temperature = 0.95,
)

write_wav("output.wav", 24000, output_dict["wav"])