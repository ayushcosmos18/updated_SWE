from tkinter import*
from tkinter import messagebox
import ast

import tkinter as tk

window=Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.attributes('-fullscreen', True)
window.overrideredirect(False)

def signup():
    username=user.get()
    password=code.get()
    confirm_password=confirm.get()
    if password==confirm_password:
        try:
            file=open('datasheet.txt', 'r+')
            d=file.read()
            r=ast.literal_eval(d)
            
            dict2={username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()
            
            file=open('datasheet.txt', 'w')
            w=file.write(str(r))
            messagebox.showinfo('Signup', 'Sucessfully sign up')
        except:
            file=open('datasheet.txt','w')
            pp=str({'Username':'password'})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror('Invalid',"Both Password should match")

def sign():
    window.destroy()


img =PhotoImage(file='signup.png')
Label(window,image=img,border=0,bg='white').pack()

frame = tk.Frame(window, bg="white")
frame.pack(expand=True)

heading=Label(frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.pack(pady=(50,20))
#####
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0, 'Username')

user=Entry(frame, width=25, fg='black', border=0,bg='white', font=('Microsoft Yahei UI Light',11))
user.pack(pady=10)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame,width=295,height=2, bg='black').pack()

####

def on_enter1(e):
    code.delete(0, 'end')
def on_leave1(e):
    if code.get()=='':
        code.insert(0, 'Password')

code=Entry(frame, width=25, fg='black', border=0,bg='white', font=('Microsoft Yahei UI Light',11))
code.pack(pady=10)
code.insert(0, 'Password')
code.config(show="*")
code.bind("<FocusIn>", on_enter1)
code.bind("<FocusOut>", on_leave1)
Frame(frame,width=295,height=2, bg='black').pack()

####

def on_enter2(e):
    confirm.delete(0, 'end')
def on_leave2(e):
    if confirm.get()=='':
        confirm.insert(0, 'Password')

confirm=Entry(frame, width=25, fg='black', border=0,bg='white', font=('Microsoft Yahei UI Light',11))
confirm.pack(pady=10)
confirm.insert(0, 'Password')
confirm.config(show="*")
confirm.bind("<FocusIn>", on_enter2)
confirm.bind("<FocusOut>", on_leave2)
Frame(frame,width=295,height=2, bg='black').pack()

Button (frame, width=39, pady=7,text='Sign up', bg='#57a1f8', fg='white', border=0,command=signup). pack(pady=20)

label=Label (frame,text='I have an account', fg='black', bg='white', font=( 'Microsoft YaHei UI Light', 9))
label.pack()
signin=Button(frame, width=6, text='Sign in', border=0,bg='white', cursor= 'hand2',fg='#57a1f8',command=sign)
signin.pack()

window.mainloop()