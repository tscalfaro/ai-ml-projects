import asyncio
import requests
import speech_recognition as sr
import os
from rapidfuzz import fuzz, process as fuzzy_process
from command_map import COMMAND_MAP
from tts_engine import speak
exit_event = asyncio.Event()

FUZZY_THRESHOLD = 75
OLLAMA_URL = "http://localhost:11434/api/generate"
TERMINATORS = {"goodbye", "stop", "exit", "shutdown", "shut down", "quit"}

def process_command(command: str) -> str:
    command = command.lower().strip()
    
    #Extract triggers from map
    triggers = [trigger for trigger, _ in COMMAND_MAP]

    #Find the best fuzzy match
    match, score, idx = fuzzy_process.extractOne(command, triggers, scorer=fuzz.partial_ratio)

    if score >= FUZZY_THRESHOLD:
        action = COMMAND_MAP[idx][1]
        return action()
    return "Sorry, I did not understand that command."

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

        # Handle local commands before calling ollama
        response = process_command(query)
        if "did not understand" not in response.lower():
            print(f"\nJarvis: {response}")
            await speak(response)
        else:
            await ask_ollama(query)

if __name__ == "__main__":
    try:
        asyncio.run(start_assistant())
    except (KeyboardInterrupt, SystemExit):
        exit_event.set()
        print("\n[Interrupted - shutting down cleanly]")