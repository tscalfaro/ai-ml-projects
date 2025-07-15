import pvporcupine
import pyaudiowpatch as pyaudio
import struct
import os
from dotenv import load_dotenv
from assistant import start_assistant

load_dotenv()
access_key = os.getenv("PORCUPINE_ACCESS_KEY")

def main():

    if not access_key:
        raise ValueError("Access key not found in .env file!")

    porcupine = pvporcupine.create(access_key=access_key, keywords=["jarvis"])
    pa = pyaudio.PyAudio()

    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length,
    )

    print("Listening for wake word...")

    try:
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            result = porcupine.process(pcm)
            if result >= 0:
                print("Wake word detected!")
                start_assistant()
                print("Returned to wake word listening...")

    except KeyboardInterrupt:
        print("Stopping...")

    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()

if __name__ == "__main__":
    main()