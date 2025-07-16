import asyncio
import requests
import speech_recognition as sr
from tts_engine import speak
exit_event = asyncio.Event()

OLLAMA_URL = "http://localhost:11434/api/generate"
TERMINATORS = {"goodbye", "stop", "exit", "shutdown", "shut down", "quit"}

async def listen():
    def blocking_listen():
        r = sr.Recognizer()
        r.pause_threshold = 1.5
        r.energy_threshold = 600
        with sr.Microphone() as source:
            print("Mic Listening...")
            audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return "Speech service unavailable"

    return await asyncio.to_thread(blocking_listen)

async def ask_ollama(prompt: str) -> None:
    import requests
    import json
    
    def stream():
        with requests.post(
            OLLAMA_URL,
            json={"model": "llama3", "prompt": prompt},
            stream=True,
            timeout=30,
        ) as r:
            for raw in r.iter_lines():
                if raw:
                    yield json.loads(raw.decode())["response"]


    full = []
    print("\nJarvis:", end="", flush=True)

    for chunk in stream():
        print(chunk, end="", flush=True)
        full.append(chunk)
    
    await speak("".join(full))

async def start_assistant():
    while not exit_event.is_set():
        query = (await listen()).strip().lower()
        if not query:
            continue    # User was silent
        
        if any(word in query for word in TERMINATORS):
            print("\nJarvis: Farewell!")
            await speak("Good-bye!")
            exit_event.set()
            break

        await ask_ollama(query)

if __name__ == "__main__":
    try:
        asyncio.run(start_assistant())
    except (KeyboardInterrupt, SystemExit):
        exit_event.set()
        print("\n[Interrupted - shutting down cleanly]")