import pyautogui
import time
from actions import perform_action

class GestureController:
    def __init__(self):
        self.prev_action = None
        self.last_action_time = time.time()

    def detect_gesture(self, lmList):
        if not lmList:
            return None

        fingers = self.finger_states(lmList)

        if fingers == [0, 1, 0, 0, 0]:
            return "point"
        elif fingers == [0, 0, 0, 0, 0]:
            return "fist"
        elif fingers == [1, 1, 1, 1, 1]:
            return "open_palm"
        elif fingers == [1, 0, 0, 0, 0]:
            return "thumbs_up"
        elif fingers == [0, 0, 0, 0, 1]:
            return "thumbs_down"
        elif fingers == [0, 1, 1, 0, 0]:
            return "two_fingers"
        elif fingers == [0, 1, 0, 0, 1]:
            return "screenshot"
        elif fingers == [1, 0, 0, 1, 1]:
            return "stealth_mode"
        return None

    def finger_states(self, lm):
        tipIds = [4, 8, 12, 16, 20]
        fingers = []
        fingers.append(1 if lm[tipIds[0]][1] < lm[tipIds[0] - 1][1] else 0)
        for id in range(1, 5):
            fingers.append(1 if lm[tipIds[id]][2] < lm[tipIds[id] - 2][2] else 0)
        return fingers

    def act(self, gesture, lmList):
        now = time.time()
        cooldown = 1.0

        if gesture == "point" and lmList:
            index_finger = lmList[8]
            screen_w, screen_h = pyautogui.size()
            frame_w, frame_h = 640, 480
            x = int(index_finger[1] * screen_w / frame_w)
            y = int(index_finger[2] * screen_h / frame_h)
            pyautogui.moveTo(x, y)
        elif gesture and (gesture != self.prev_action or now - self.last_action_time > cooldown):
            perform_action(gesture)
            self.prev_action = gesture
            self.last_action_time = now
