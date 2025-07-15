import requests
import speech_recognition as sr
from tts_engine import speak




def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mic Listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Speech service unavailable"

def ask_ollama(prompt):
    import requests
    import json
    

    response = requests.post(
        'http://localhost:11434/api/generate',
        json={"model": "llama3", "prompt": prompt},
        stream=True
    )

    full_response = ""
    print("\nAssistant:", end="")

    for line in response.iter_lines():
        if line:
            try:
                parsed_line = json.loads(line.decode("utf-8"))
                word = parsed_line.get("response", "")
                print(word, end="", flush=True)
                full_response += word
            except json.JSONDecodeError as e:
                print(f"\n[Error parsing line] {line}\n")
    
    print("\n\nSpeaking response...\n")
    speak(full_response)

def start_assistant():
    while True:
        query = listen()
        
        if query:
            termination_phrases = ["goodbye", "stop", "exit", "shutdown", "shut down", "quit"]
            if any(phrase in query.lower() for phrase in termination_phrases):
                print("Shutting down assistant...")
                speak("Goodbye!")
                break  # Exit the loop

            ask_ollama(query)

if __name__ == "__main__":
    start_assistant()