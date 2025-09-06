# Group 2
# Crisostomo, Alessandro
# Ramos, Gab
# Senatin, Christopher

import tkinter as tk
from tkmacosx import Button
import cv2

# Cyndaquill colors
# Main Color 
CYND_BODY = "#306B84"
CYND_BELLY = "#FFF7A5"

# OpenCV
def foo():
    print("Hello World")


# Tkinter
root = tk.Tk()
root.title("Group 2 - Mini Project")
root.geometry("640x520")
root.configure(bg=CYND_BODY)

btn = Button(
    root,
    text="Start",
    command=foo,
    bg=CYND_BELLY,
    padx=20,
    pady=10,
    borderless=True,
)
btn.pack(expand=True)

root.mainloop()

