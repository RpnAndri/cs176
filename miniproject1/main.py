# Group 2
# Crisostomo, Alessandro
# Ramos, Gab
# Senatin, Christopher

import tkinter as tk
from tkmacosx import Button
from PIL import Image, ImageTk
import cv2

# Global Variables
cap = None
running = False

WIDTH = 500
HEIGHT = 300

# Cyndaquill colors
# Main Color 
CYND_BODY = "#306B84"
CYND_BELLY = "#FFF7A5"
CYND_RED = "#FF3701"



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

