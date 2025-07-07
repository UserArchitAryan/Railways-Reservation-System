from tkinter import *
from tkinter import messagebox
import os

def checkLogin():
    username = userName.get()
    messagebox.showinfo("Welcome", f"Welcome back, {username}!")
    os.system('python "F:\Railways Reservation\information panal.py"')

root = Tk()
root.title("Login")
root.minsize(width=400, height=400)
root.geometry("600x500")

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

headingLabel = Label(headingFrame1, text="Login", bg='black', fg='white', font=('Courier', 15, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

labelFrame = Frame(root, bg='grey')
labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

# Enter User Name
lb1 = Label(labelFrame, text="User Name : ", bg='grey', fg='white')
lb1.place(relx=0.05, rely=0.2, relheight=0.08)

userName = Entry(labelFrame)
userName.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

lb2 = Label(labelFrame, text="Password : ", bg='grey', fg='white')
lb2.place(relx=0.05, rely=0.35, relheight=0.08)

password = Entry(labelFrame, show="*")
password.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

# Submit Button
SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=checkLogin)
SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

root.mainloop()
