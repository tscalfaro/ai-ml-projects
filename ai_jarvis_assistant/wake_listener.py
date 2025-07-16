import pvporcupine
import pyaudiowpatch as pyaudio
import struct
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
access_key = os.getenv("PORCUPINE_ACCESS_KEY")

async def wake_listener():
    from assistant import start_assistant, exit_event

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
        while not exit_event.is_set():
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            result = porcupine.process(pcm)
            if result >= 0:
                print("Wake word detected!")
                await start_assistant()
                print("Returned to wake word listening...")

    except KeyboardInterrupt:
        print("Stopping...")

    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()
        exit_event.set()

if __name__ == "__main__":
    import assistant
    try:
        asyncio.run(wake_listener())
    except KeyboardInterrupt:
        print("\n[INFO] KeyboardInterrupt received. Shutting down gracefully...")
    except asyncio.CancelledError:
        print("\n[INFO] Asyncio task was cancelled.")
    finally:
        assistant.exit_event.set()