from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import random
import subprocess
import pandas as pd 
import numpy as np 
import pickle 
import ast
import mediapipe as mp
import cv2
from PIL import Image, ImageTk 

from landmarks import landmarks
import customtkinter as ck 

image_paths = ['Can.png', 'Can2.png']
image_path = random.choice(image_paths)


pil_image=Image.open(image_path)

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import subprocess

def signup_command():
    subprocess.Popen(["python", "SignUp_page.py"])
    root.destroy()

def signin():
    username = user.get()
    password = code.get()

    file=open('datasheet.txt', 'r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
    print (r.keys())
    print (r.values())

    if username in r.keys() and password==r[username]:
        subprocess.Popen(["python", "app.py"])
        root.destroy()
    else:
        messagebox.showerror('Invalid','Invalid username or password')
def on_enter(e):
    if user.get() == 'Username':
        user.delete(0, 'end')

def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')

def on_enter1(e):
    if code.get() == 'Password':
        code.delete(0, 'end')

def on_leave1(e):
    if code.get() == '':
        code.insert(0, 'Password')

root = tk.Tk()

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set full screen and remove window decorations
root.attributes('-fullscreen', True)
root.overrideredirect(False)

root.configure(bg='#fff')

image_paths = ['Can.png', 'Can2.png']
image_path = random.choice(image_paths)
pil_image = Image.open(image_path)
img = ImageTk.PhotoImage(pil_image)
tk.Label(root, image=img, bg='white').pack()

frame = tk.Frame(root, bg="white")
frame.pack(expand=True)

heading = tk.Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.pack(pady=(50, 20))

user = tk.Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.pack(pady=10)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

tk.Frame(frame, width=295, height=2, bg='black').pack()

code = tk.Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.pack(pady=10)
code.insert(0, 'Password')
code.config(show="*")
code.bind('<FocusIn>', on_enter1)
code.bind('<FocusOut>', on_leave1)

tk.Frame(frame, width=295, height=2, bg='black').pack()

tk.Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).pack(pady=20)

tk.Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9)).pack()

tk.Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',command=signup_command).pack()

root.mainloop()
