import cv2
import tkinter as tk
from hand_tracking import HandDetector
from gesture_controller import GestureController

root = tk.Tk()
root.title("Gesture HUD")
root.geometry("300x60+10+10")
root.configure(bg='black')
root.attributes("-topmost", True)
root.overrideredirect(True)

label = tk.Label(root, text="Initializing...", font=("Consolas", 16), fg="cyan", bg="black")
label.pack()

root.update()

cap = cv2.VideoCapture(0)
detector = HandDetector()
controller = GestureController()

while True:
    success, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame)

    gesture = controller.detect_gesture(lmList)
    controller.act(gesture, lmList)

    label.config(text=f"Gesture: {gesture}")
    root.update()

    cv2.imshow("Gesture Controller", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
root.destroy()
