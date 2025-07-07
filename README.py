from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Ensure the image file exists
image_path = "F:\Railways Reservation\Your paragraph text.png"
if not os.path.exists(image_path):
    raise FileNotFoundError(f"The image file was not found: {image_path}")

root = Tk()
root.title("Welcome to Automated Railways Yathra Application")
root.geometry("1350x700+0+0")
root.config(bg="black")

homelogo = Image.open(image_path)
homelogo = ImageTk.PhotoImage(homelogo)
homelogo_label = Label(root, image=homelogo, bg="white")
homelogo_label.grid(row=0, column=0, padx=10, pady=5)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

caption = Label(root, text="A.R.Y.A", font=("times new roman", 50, "bold"), bg="black", fg="white")
caption.place(x=830, y=790)

def open_login():
    os.system('python "F:\Railways Reservation\login.py"')

# Add login button under the text "A.R.Y.A"
login_button = Button(root, text="Login", font=("times new roman", 20, "bold"), bg="gray", fg="white", command=open_login)
login_button.place(x=910, y=880)

# Start the main loop
root.mainloop()
