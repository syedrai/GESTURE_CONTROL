import speech_recognition as sr
import pyautogui
import keyboard
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def handle_voice_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening for voice command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"[VOICE] {command}")
        speak(f"You said: {command}")

        if "open notepad" in command:
            pyautogui.press("win")
            pyautogui.write("notepad")
            pyautogui.press("enter")
        elif "refresh" in command:
            keyboard.press_and_release("f5")
        elif "next tab" in command:
            keyboard.press_and_release("ctrl+tab")
        elif "previous tab" in command:
            keyboard.press_and_release("ctrl+shift+tab")
        elif "close tab" in command:
            keyboard.press_and_release("ctrl+w")
        elif "open chrome" in command:
            pyautogui.press("win")
            pyautogui.write("chrome")
            pyautogui.press("enter")
        else:
            speak("Command not recognized")

    except sr.UnknownValueError:
        print("Could not understand audio")
        speak("I didn't catch that")
    except sr.RequestError:
        print("API unavailable")
        speak("Speech recognition service failed")