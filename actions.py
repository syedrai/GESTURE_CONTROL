import pyautogui
import keyboard
import json
import os
import pyttsx3
from app_launcher import launch_app
from playsound import playsound

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

with open("gesture_macros.json", "r") as f:
    macros = json.load(f)

def perform_action(gesture):
    print(f"[ACTION]: {gesture}")

    if gesture in macros:
        command = macros[gesture]
        if command.startswith("launch "):
            app = command.split(" ")[1]
            launch_app(app)
            speak(f"Launching {app}")
        elif command.startswith("key:"):
            keys = command[4:]
            keyboard.press_and_release(keys)
            speak(f"Hotkey {keys} pressed")
        elif command.startswith("vol:"):
            if command == "vol:up":
                pyautogui.press("volumeup")
                speak("Volume up")
            elif command == "vol:down":
                pyautogui.press("volumedown")
                speak("Volume down")
        elif command == "click":
            pyautogui.click()
            speak("Click")
        elif command == "scroll_down":
            pyautogui.scroll(-200)
            speak("Scrolling")
        elif command == "screenshot":
            pyautogui.screenshot("gesture_shot.png")
            speak("Screenshot taken")
        elif command == "stealth":
            os.system("rundll32.exe user32.dll,LockWorkStation")
            speak("Activating stealth mode")

    sound_path = f"assets/sounds/{gesture}.wav"
    if os.path.exists(sound_path):
        playsound(sound_path)
