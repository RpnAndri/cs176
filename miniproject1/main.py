# Group 2
# Crisostomo, Alessandro
# Ramos, Gab
# Senatin, Christopher

import tkinter as tk
from tkmacosx import Button
from PIL import Image, ImageTk
import cv2
import mediapipe as mp

# Global Variables
cap = None
running = False

WIDTH = 500
HEIGHT = 300

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands = 1,
)


# Cyndaquill colors
# Main Color 
CYND_BODY = "#306B84"
CYND_BELLY = "#FFF7A5"
CYND_RED = "#FF3701"

# These numbers are seen in the documentation for the fingers' corresponding index
finger_tips = [8, 12, 16, 20]   # Index, Middle, Ring, Pinky
finger_joints = [6, 10, 14, 18] # Index, Middle, Ring, Pinky

# Count the number of fingers given the landmarks
def count_fingers(hand_landmarks, hand) -> int:
    # Simple counting algorithm
    # Not bullet-proof, exploitable if you bend your wrist
    # To be open, the tips must have a higher y value than the joints
    # The thumb is the same for the x-value, depends on left or right

    raised_fingers = 0

    # Tall fingers first
    for i in range(len(finger_tips)):
        if hand_landmarks.landmark[finger_tips[i]].y < hand_landmarks.landmark[finger_joints[i]].y:
            raised_fingers += 1

    # Thumb checker
    if hand == "Right" and hand_landmarks.landmark[4].x < hand_landmarks.landmark[2].x:
        raised_fingers += 1
    elif hand == "Left" and hand_landmarks.landmark[4].x > hand_landmarks.landmark[2].x:
        raised_fingers += 1


    return raised_fingers


# OpenCV
def start():
    global cap, running
    if not running:
        cap = cv2.VideoCapture(0)   # 0 for Webcam
        running = True
        update()

def update():
    global cap, running
    if running:
        ret, frame = cap.read()
        if ret:
            # Resize to the tkinter frame
            frame = cv2.resize(frame, (WIDTH, HEIGHT))

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw the detected fingers on the frame
                    mp_drawing.draw_landmarks(
                        frame, 
                        hand_landmarks, 
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style(),
                    )

                for hand in results.multi_handedness:
                    # Gets if left or right
                    fingers = count_fingers(hand_landmarks, hand.classification[0].label)

                    match fingers:
                        case 1:
                            print(1)
                        case 2:
                            print(2)
                        case 3:
                            print(3)
                        case 4:
                            print(4)
                        case 5:
                            print(5)
                        case _:
                            print(0)

            else:
                print(0)
                        

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)
        video_label.after(10, update)


# Tkinter
root = tk.Tk()
root.title("Group 2 - Mini Project")
root.geometry("640x520")
root.configure(bg=CYND_BODY)

BD = 5

# Video Frame
video_frame = tk.Frame(root, width=WIDTH, height=HEIGHT, bg=CYND_BODY, bd=BD, relief="solid")
video_frame.pack(pady=10)

video_label = tk.Label(video_frame, bg=CYND_RED)
video_label.place(x=0, y=0, width=WIDTH-(BD*2), height=HEIGHT-(BD*2))

btn = Button(
    root,
    text="Start",
    command=start,
    bg=CYND_BELLY,
    padx=20,
    pady=10,
    borderless=True,
)
btn.pack(expand=True)

root.mainloop()

