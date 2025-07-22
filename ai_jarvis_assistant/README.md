# AI Assistant Project Summary (July 2025)

## Project Goal
Build local/offline desktop AI assistant inspired by Jarvis, focused on voice input and TTS output with modular, scalable design

---

## Current Functionality

### Voice Interaction Pipeline
-   Wake word triggers microphone listening.
-   Captures voice input and processes it into text.
-   First tries to handle the command locally.
-   Falls back to LLM (Ollama) for anything not recognized.

### Basic Commands Implemented (via `COMMAND_MAP`)
| Command Trigger  | Action |
|------------------|--------|
| "time"           | Speaks current time |
| "date"           | Speaks current date |
| "ip address"     | Returns local IP |
| "open downloads" | Opens Downloads folder |
| "launch chrome"  | Tries launching Chrome (C: and D: drives checked) |

## Key Features
-   **Voice Acitvated** with wake word detection (Jarvis)
-   **Coqui XTTS** for hyperrealistic offline text-to-speech
-   Mic **automatically pauses durring TTS** and reliably **reopens after completion**
-   **Spoken and printed responses** handled in parallel
-   **Modular architecture** for easy future expansion (i.e scheduling, memory)

---

## Architecture

### Key Modules
-   `wake_listener.py`: Handles wake word detection and mic triggering
-   `assistant.py`: Core assistant logic for processing and routing input
-   `tts_engine.py`: Manages XTTS model and voice output
-   `command_map.py`: Maps keywords to functions for easy extensibility
-   `basic_commands.py`: Local system commands (time, IP, launch apps)

---

## Recent Updates
-   Fuzzy matching via `rapidfuzz` for more flexible command recognition
-   `process_command()` now called before LLM fallback
-   Command routing via `COMMAND_MAP` for maintainability

---

## Next Steps
-   Add task management and contextual memory
-   Consider voice-activated loggin or session summaries
-   Enhance flexibility in command parsing (NLP instead of fuzzy matching potentially)

---
