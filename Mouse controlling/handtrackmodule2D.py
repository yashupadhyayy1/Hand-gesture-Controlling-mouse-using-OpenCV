import cv2
import mediapipe as mp
import time
import math


class handDetector():
    def __init__(self, mode=False, max_hands=2, mcomplexity=1, detectionconf=0.5, trackingconf=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.mcomplexity = mcomplexity
        self.detectionconf = detectionconf
        self.trackingconf = trackingconf

        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.mode, self.max_hands, self.mcomplexity, self.detectionconf,
                                        self.trackingconf)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mphands.HAND_CONNECTIONS)
        return img

    def findPositon(self, img, handNo=0, draw=True):

        xlist = []
        ylist = []
        bbox = []
        self.lmlist = []
        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myhand.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xlist.append(cx)
                ylist.append(cy)
                self.lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)


                xmin, xmax = min(xlist), max(xlist)
                ymin, ymax = min(ylist), max(ylist)
                bbox = xmin, ymin , xmax, ymax

            if draw:
                cv2.rectangle(img, (xmin - 20,ymin - 20),(xmax + 20,ymax + 20), (0, 255, 0), 2)

        return self.lmlist, bbox

    def fingerUp(self):
        fingers = []
        #thumb
        if self.lmlist[self.tipIds[0]][1]> self.lmlist[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # Fingers
        for id in range(1,5):
            if self.lmlist[self.tipIds[id]][2] > self.lmlist[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        # Total Fingers
        return fingers

    def findDistance(self, p1, p2, img, draw=True, r=15, t=3):
        x1, y1 = self.lmlist[p1][1:]
        x2, y2 = self.lmlist[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
            cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (cx, cy), r, (255, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)

        return length, img, [x1, y1, x2, y2, cx, cy]


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist, bbox = detector.findPositon(img)
        if len(lmlist) != 0:
            print(lmlist[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        cv2.imshow('image', img)
        key = cv2.waitKey(25) & 0xFF
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
