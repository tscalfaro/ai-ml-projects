import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)
    
def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def remember(key, value):
    data = load_memory()
    data[key] = value
    save_memory(data)
    return f"I'll remember that {key} is {value}."

def recall(key):
    data = load_memory()
    return data.get(key, f"I don't know what your {key} is.")

def forget(key):
    data = load_memory()
    if key in data:
        del data[key]
        save_memory(data)
        return f"I forgot your {key}."
    return f"I don't have any memory of your {key}."

def handle_remember(command: str) -> str:
    try:
        stripped = command.lower().replace("remember that", "").strip()
        if " is " not in stripped:
            return "Please use the format: remember that [key] is [value]"
        key, value = stripped.split(" is ", 1)
        return remember(key.strip(), value.strip())
    except Exception as e:
        return f"Could not remember that: {str(e)}"
    
def handle_recall(command: str) -> str:
    try:
        key = command.lower().replace("what's ", "").replace("what is ", "").strip()
        return recall(key)
    except Exception as e:
        return f"Could not recall that: {str(e)}"
    
def handle_forget(command: str) -> str:
    try:
        key = command.lower().replace("forget ", "").strip()
        return forget(key)
    except Exception as e:
        return f"Could not forget that: {str(e)}"