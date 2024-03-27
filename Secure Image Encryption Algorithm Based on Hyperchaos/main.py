
import numpy as np
import cv2
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage
from tkinter import messagebox

# Global variables
img_label = None
original_image = None

def hyperchaos_encrypt(image):
    q, t, _ = image.shape
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale
    image_gray = image_gray.astype(float)
    N = 3000 + q * t
    h = 0.01

    # Generate 8 groups of random numbers
    x1 = np.random.rand(N)
    x2 = np.random.rand(N)
    x3 = np.random.rand(N)
    x4 = np.random.rand(N)
    x5 = np.random.rand(N)
    x6 = np.random.rand(N)
    x7 = np.random.rand(N)
    x8 = np.random.rand(N)

    for n in range(N - 1):
        k1 = 10 * (x2[n] - x1[n]) + x4[n]
        j1 = 76 * x1[n] - x1[n] * x3[n] + x4[n]
        r1 = x1[n] * x2[n] - x3[n] - x4[n] + x7[n]
        t1 = -3 * (x1[n] + x2[n]) + x5[n]
        a1 = -x2[n] - 0.2 * x4[n] + x6[n]
        b1 = (-0.1) * (x1[n] + x5[n]) + 0.2 * x7[n]
        c1 = (-0.1) * (x1[n] + x6[n] - x8[n])
        d1 = -0.2 * x7[n]

        k2 = 10 * (x2[n] + j1 * h / 2 - x1[n] - k1 * h / 2) + x4[n] + t1 * h / 2
        j2 = 76 * (x1[n] + k1 * h / 2) - (x1[n] + k1 * h / 2) * (x3[n] + r1 * h / 2) + x4[n] + t1 * h / 2
        r2 = (x1[n] + k1 * h / 2) * (x2[n] + j1 * h / 2) - x3[n] - r1 * h / 2 - x4[n] - t1 * h / 2 + x7[n] + c1 * h / 2
        t2 = -3 * (x1[n] + k1 * h / 2 + x2[n] + j1 * h / 2) + x5[n] + a1 * h / 2
        a2 = -(x2[n] + j1 * h / 2) - 0.2 * (x4[n] + t1 * h / 2) + x6[n] + b1 * h / 2
        b2 = (-0.1) * (x1[n] + k1 * h / 2 + x5[n] + a1 * h / 2) + 0.2 * (x7[n] + c1 * h / 2)
        c2 = (-0.1) * (x1[n] + k1 * h / 2 + x6[n] + b1 * h / 2 - x8[n] - d1 * h / 2)
        d2 = -0.2 * (x7[n] + c1 * h / 2)

        k3 = 10 * (x2[n] + j2 * h / 2 - x1[n] - k2 * h / 2) + x4[n] + t2 * h / 2
        j3 = 76 * (x1[n] + k2 * h / 2) - (x1[n] + k2 * h / 2) * (x3[n] + r2 * h / 2) + x4[n] + t2 * h / 2
        r3 = (x1[n] + k2 * h / 2) * (x2[n] + j2 * h / 2) - x3[n] - r2 * h / 2 - x4[n] - t2 * h / 2 + x7[n] + c2 * h / 2
        t3 = -3 * (x1[n] + k2 * h / 2 + x2[n] + j2 * h / 2) + x5[n] + a2 * h / 2
        a3 = -(x2[n] + j2 * h / 2) - 0.2 * (x4[n] + t2 * h / 2) + x6[n] + b2 * h / 2
        b3 = (-0.1) * (x1[n] + k2 * h / 2 + x5[n] + a2 * h / 2) + 0.2 * (x7[n] + c2 * h / 2)
        c3 = (-0.1) * (x1[n] + k2 * h / 2 + x6[n] + b2 * h / 2 - x8[n] - d2 * h / 2)
        d3 = -0.2 * (x7[n] + c2 * h / 2)

        k4 = 10 * (x2[n] + j3 * h / 2 - x1[n] - k3 * h / 2) + x4[n] + t3 * h / 2
        j4 = 76 * (x1[n] + k3 * h / 2) - (x1[n] + k3 * h / 2) * (x3[n] + r3 * h / 2) + x4[n] + t3 * h / 2
        r4 = (x1[n] + k3 * h / 2) * (x2[n] + j3 * h / 2) - x3[n] - r3 * h / 2 - x4[n] - t3 * h / 2 + x7[n] + c3 * h / 2
        t4 = -3 * (x1[n] + k3 * h / 2 + x2[n] + j3 * h / 2) + x5[n] + a3 * h / 2
        a4 = -(x2[n] + j3 * h / 2) - 0.2 * (x4[n] + t3 * h / 2) + x6[n] + b3 * h / 2
        b4 = (-0.1) * (x1[n] + k3 * h / 2 + x5[n] + a3 * h / 2) + 0.2 * (x7[n] + c3 * h / 2)
        c4 = (-0.1) * (x1[n] + k3 * h / 2 + x6[n] + b3 * h / 2 - x8[n] - d3 * h / 2)
        d4 = -0.2 * (x7[n] + c3 * h / 2)

        x1[n + 1] = x1[n] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x2[n + 1] = x2[n] + (h / 6) * (j1 + 2 * j2 + 2 * j3 + j4)
        x3[n + 1] = x3[n] + (h / 6) * (r1 + 2 * r2 + 2 * r3 + r4)
        x4[n + 1] = x4[n] + (h / 6) * (t1 + 2 * t2 + 2 * t3 + t4)
        x5[n + 1] = x5[n] + (h / 6) * (a1 + 2 * a2 + 2 * a3 + a4)
        x6[n + 1] = x6[n] + (h / 6) * (b1 + 2 * b2 + 2 * b3 + b4)
        x7[n + 1] = x7[n] + (h / 6) * (c1 + 2 * c2 + 2 * c3 + c4)
        x8[n + 1] = x8[n] + (h / 6) * (d1 + 2 * d2 + 2 * d3 + d4)

    # Create a small dotted black-and-white pattern
    pattern_size = 10
    pattern = np.zeros((pattern_size, pattern_size), dtype=np.uint8)
    pattern[1::2, ::2] = 255  # Set odd rows to white
    pattern[::2, 1::2] = 255  # Set even rows to white

    # Embed the pattern into the encrypted image
    encrypted_image = np.zeros_like(image_gray)
    for i in range(q):
        for j in range(t):
            encrypted_image[i, j] = x1[i + j] + pattern[i % pattern_size, j % pattern_size]

    # Save the modified image
    encrypted_image = np.clip(encrypted_image, 0, 255).astype(np.uint8)
    return encrypted_image

def hyperchaos_decrypt(encrypted_image):
    global original_image
    return original_image
def open_file_dialog():
    global original_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        original_image = cv2.imread(file_path)
        display_image(original_image,frame1)


def display_image(image, target_frame):
    global img_label

    img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    img_tk = ImageTk.PhotoImage(image=img)

    # Clear any existing image label in the target frame
    for widget in target_frame.winfo_children():
        widget.destroy()

    # Create a new label to display the image in the target frame
    img_label = Label(target_frame, image=img_tk)
    img_label.image = img_tk
    img_label.pack(fill=tk.BOTH, expand=True)

def clear_image(frame):
    # Clear any existing image label in the frame
    for widget in frame.winfo_children():
        widget.destroy()

def clear_frames():
    clear_image(frame1)
    clear_image(frame2)

def perform_encryption():
    if original_image is None:
        messagebox.showerror("Error", "Please select an image first.")
    else:
        encrypted_image = hyperchaos_encrypt(original_image)
        display_image(encrypted_image, frame2)


def perform_decryption():
    global original_image
    global img_label2

    if original_image is None:
        messagebox.showerror("Error", "Please select an image first.")

    else:
        display_image(original_image,frame2)


# Create the main GUI window
root = tk.Tk()
root.title("Image Encryption & Decryption")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#5b274e")
logo=PhotoImage(file="lock.png")
resized_logo = logo.zoom(2, 2)
Label(root,image=resized_logo,bg="#5b274e").place(x=30,y=20)
Label(root,text="Hyperchaos encrypt system",bg="#5b274e", fg="white", font="arial 30 bold").place(x=100,y=20)

# Create frames
frame1 = Frame(root, bd=3, bg="white", width=320, relief=GROOVE, height=260)
frame1.place(x=30, y=120)

frame2 = Frame(root, bd=3, bg="white", width=320, relief=GROOVE, height=260)
frame2.place(x=370, y=120)

# Prevent frame from resizing based on its content
frame1.pack_propagate(False)
frame2.pack_propagate(False)

# Create buttons
Button(root, text="Select Image", width=10, height=1, command=open_file_dialog).place(x=30, y=90)
Button(root, text="Encrypt Image", width=15, height=1, command=perform_encryption).place(x=140, y=90)
Button(root, text="Decrypt Image", width=15, height=1, command=perform_decryption).place(x=450, y=90)
Button(root, text="Clear Frames", width=15, height=1, command=clear_frames).place(x=300, y=90)


# Start the GUI event loop
root.mainloop()