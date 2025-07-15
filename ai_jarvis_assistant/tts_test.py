import torch
from torch.serialization import add_safe_globals
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs  
from TTS.config.shared_configs import BaseDatasetConfig 

# Allowlist both necessary classes
add_safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs])

from TTS.api import TTS
import os

# Load the model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

text = "Good day. I am your assistant, ready to help you."

os.makedirs("voice_tests", exist_ok=True)

tts.tts_to_file(
    text=text,
    speaker_wav="voice_sample/good_morning_jarvis.wav",
    language="en",
    file_path=f"voice_tests/output.wav"
)
