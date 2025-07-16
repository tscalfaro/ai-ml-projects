# AI Assistant Project Summary (July 2025)

## Project Goal
Build local/offline desktop AI assistant inspired by Jarvis, focused on voice input and TTS output with modular, scalable design

## Key Features
-   **Voice Acitvated** with wake word detection (Jarvis)
-   **Coqui XTTS** for hyperrealistic offline text-to-speech
-   Mic **automatically pauses durring TTS** and reliably **reopens after completion**
-   **Spoken and printed responses** handled in parallel
-   **Modular architecture** for easy future expansion (i.e scheduling, memory)

## Current Architecture
-   `wake_listener.py`: Handles wake word detection and mic triggering
-   `assistant.py`: Core assistant logic for processing and routing input
-   `tts_engine.py`: Manages XTTS model and voice output

## Resolved Issues
-   Mic reopening now works reliably across runs
-   No more need for manual exits - concurrency issues have been resolved
-   Slight slowdown in long sessions, but not disruptive

---
