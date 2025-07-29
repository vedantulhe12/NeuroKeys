import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller
from time import sleep

# Initialize
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
keyboard = Controller()

keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
    ["<", " ", "Enter"]
]

finalText = ""

class Button:
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text
        self.hoverCount = 0 

    def isInside(self, point):
        x, y = self.pos
        w, h = self.size
        return x < point[0] < x + w and y < point[1] < y + h

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h),
                      (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img

# Create button list
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    img = drawAll(img, buttonList)

    if hands:
        lmList = hands[0]["lmList"]
        indexTip = lmList[8][:2]

        for button in buttonList:
            if button.isInside(indexTip):
                button.hoverCount += 1
                # Visual feedback while hovering
                x, y = button.pos
                w, h = button.size
                cv2.rectangle(img, button.pos, (x + w, y + h),
                              (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

                if button.hoverCount > 30:  # 1 second
                    print(f"Pressed: {button.text}")
                    keyboard.press(button.text)
                    keyboard.release(button.text)

                    if button.text == '<':
                        finalText = finalText[:-1]
                    elif button.text == 'Enter':
                        finalText += '\n'
                    else:
                        finalText += button.text

                    button.hoverCount = 0
                    sleep(0.3)  
            else:
                button.hoverCount = 0

    # Show the typed text
    cv2.rectangle(img, (50, 400), (700, 500), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 470),
                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

    cv2.imshow("Virtual Keyboard", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
