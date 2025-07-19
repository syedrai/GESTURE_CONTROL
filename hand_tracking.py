import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, maxHands=1, detectionCon=0.7):
        self.handsModule = mp.solutions.hands
        self.hands = self.handsModule.Hands(max_num_hands=maxHands, min_detection_confidence=detectionCon)
        self.draw = mp.solutions.drawing_utils

    def findHands(self, frame, draw=True):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.draw.draw_landmarks(frame, handLms, self.handsModule.HAND_CONNECTIONS)
        return frame

    def findPosition(self, frame, handNo=0):
        lmList = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(hand.landmark):
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))
        return lmList