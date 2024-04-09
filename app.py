import tkinter as tk 
import customtkinter as ck 

import pandas as pd 
import numpy as np 
import pickle 

import mediapipe as mp
import cv2
from PIL import Image, ImageTk 

from landmarks import landmarks


window = tk.Tk()
window.geometry("925x500+300+200")
window.title("Exercise Tracker") 
ck.set_appearance_mode("dark")

window.attributes('-fullscreen',True)
window.overrideredirect(False)


from PIL import Image, ImageTk

# Load your PNG image


classLabel = ck.CTkLabel(window, height=40, width=120, font=('Microsoft Yahei UI Light',25,'bold'), text_color="black", padx=10)
classLabel.place(x=10, y=1)
classLabel.configure(text='STAGE') 
counterLabel = ck.CTkLabel(window, height=40, width=120, font=('Microsoft Yahei UI Light',25,'bold'), text_color="black", padx=10)
counterLabel.place(x=160, y=1)
counterLabel.configure(text='REPS') 
probLabel  = ck.CTkLabel(window, height=40, width=120, font=('Microsoft Yahei UI Light',25,'bold'), text_color="black", padx=10)
probLabel.place(x=300, y=1)
probLabel.configure(text='PROB') 
classBox = ck.CTkLabel(window, height=40, width=120, font=('Microsoft Yahei UI Light',25,'bold'), text_color="black", fg_color="#c6dbff")
classBox.place(x=10, y=41)
classBox.configure(text='0') 
counterBox = ck.CTkLabel(window, height=40, width=120, font=('Microsoft Yahei UI Light',25,'bold'), text_color="black", fg_color="#c6dbff")
counterBox.place(x=160, y=41)
counterBox.configure(text='0') 
probBox = ck.CTkLabel(window, height=40, width=120, font=('Microsoft Yahei UI Light',25,'bold'), text_color="black", fg_color="#c6dbff")
probBox.place(x=300, y=41)
probBox.configure(text='0') 
exercise_label = ck.CTkLabel(window, height=40, width=120, font=('Microsoft Yahei UI Light',35,"bold"), text_color="black")
exercise_label.place(relx=0.5, y=15, anchor="center")  # Position at the top center
exercise_label.configure(text='Deadlifts')

def reset_counter(): 
    global counter
    counter = 0 

button = ck.CTkButton(window, text='RESET', command=reset_counter, height=40, width=120, font=('Microsoft Yahei UI Light',25,'bold'), text_color="black", fg_color="#c6dbff")
button.place(x=10, y=600)

frame = tk.Frame(height=480, width=480)
frame.place(x=10, y=90) 
lmain = tk.Label(frame) 
lmain.place(x=0, y=0) 


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5) 

with open('deadlift.pkl', 'rb') as f: 
    model = pickle.load(f) 

cap = cv2.VideoCapture(1)
current_stage = ''
counter = 0 
bodylang_prob = np.array([0,0]) 
bodylang_class = '' 


def detect(): 
    global current_stage
    global counter
    global bodylang_class
    global bodylang_prob 

     
    ret, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    results = pose.process(image)
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, 
        mp_drawing.DrawingSpec(color=(106,13,173), thickness=4, circle_radius = 5), 
        mp_drawing.DrawingSpec(color=(255,102,0), thickness=5, circle_radius = 10)) 

    try: 
        row = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten().tolist()
        X = pd.DataFrame([row], columns = landmarks) 
        bodylang_prob = model.predict_proba(X)[0]
        bodylang_class = model.predict(X)[0] 

        if bodylang_class =="down" and bodylang_prob[bodylang_prob.argmax()] > 0.7: 
            current_stage = "down" 
            image_path = "down1.png"
            img_png = Image.open(image_path)  # Load the PNG image

# Resize the image if needed
            img_png = img_png.resize((460, 480))  # Adjust size as per your requirement

# Convert the image for Tkinter
            img_png_tk = ImageTk.PhotoImage(img_png)

# Create a Label to display the image
            image_label = tk.Label(window, image=img_png_tk)
            image_label.place(x=480, y=90)  # Place on the right half of the screen

# Ensure to keep a reference to the image to avoid garbage collection
            image_label.img_png_tk = img_png_tk

        elif current_stage == "down" and bodylang_class == "up" and bodylang_prob[bodylang_prob.argmax()] > 0.7:
            current_stage = "up"
            image_path = "up1.png"
            img_png = Image.open(image_path)  # Load the PNG image

# Resize the image if needed
            img_png = img_png.resize((460, 480))  # Adjust size as per your requirement

# Convert the image for Tkinter
            img_png_tk = ImageTk.PhotoImage(img_png)

# Create a Label to display the image
            image_label = tk.Label(window, image=img_png_tk)
            image_label.place(x=480, y=90)  # Place on the right half of the screen

# Ensure to keep a reference to the image to avoid garbage collection
            image_label.img_png_tk = img_png_tk 
            counter += 1 

        

    except Exception as e: 
        print(e) 

    img = image[:, :460, :] 
    imgarr = Image.fromarray(img) 
    imgtk = ImageTk.PhotoImage(imgarr) 
    lmain.imgtk = imgtk 
    lmain.configure(image=imgtk)
    lmain.after(10, detect)  

    counterBox.configure(text=counter) 
    probBox.configure(text=bodylang_prob[bodylang_prob.argmax()]) 
    classBox.configure(text=current_stage) 

detect() 
window.mainloop()

