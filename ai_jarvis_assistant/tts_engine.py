import os
from TTS.api import TTS
# from torch.serialization import add_safe_globals
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs  
from TTS.config.shared_configs import BaseDatasetConfig 

# Trust model-specific configs
#add_safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs])

tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")
SPEAKER_WAV = "voice_sample/good_morning_jarvis.wav"

def speak(text):
    os.makedirs("output", exist_ok=True)
    output_path = "output/response.wav"

    tts.tts_to_file(
        text=text,
        speaker_wav=SPEAKER_WAV,
        language="en",
        file_path=output_path
    )

    try:
        import sounddevice as sd
        import soundfile as sf
        data, fs = sf.read(output_path)
        sd.play(data, fs)
        sd.wait()
    except ImportError:
        os.system(f'start {output_path}')