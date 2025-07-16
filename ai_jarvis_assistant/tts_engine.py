import os
from TTS.api import TTS
import numpy as np
import sounddevice as sd
import asyncio
import textwrap

MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
SPEAKER_WAV = "voice_sample/jarvis.wav"

tts = TTS(model_name=MODEL_NAME, progress_bar=False, gpu=False)

async def play_audio(wav, sample_rate):
    sd.play(wav, samplerate=sample_rate)
    await asyncio.sleep(len(wav) / sample_rate)
    sd.stop()

def chunk_text(text, max_chars=250):
    import re
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= max_chars:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

async def speak(text):
    print("\nSpeaking response...")
    chunks = chunk_text(text)

    for chunk in chunks:
        if not chunk.strip():
            continue
        
        wav = tts.tts(
            text=chunk,
            speaker_wav=SPEAKER_WAV,
            language="en"
        )
        await play_audio(np.array(wav), tts.synthesizer.output_sample_rate)
    