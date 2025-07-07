import tkinter as tk
from tkinter import ttk
from time import strftime
from tkcalendar import DateEntry
import os
from fpdf import FPDF

root = tk.Tk()
root.title("Railway Reservation System")
root.geometry("1350x700")

top_bar = tk.Frame(root, bg="black", height=30)
top_bar.pack(side=tk.TOP, fill=tk.X)

def time():
    string = strftime('%H:%M:%S %p | %A | %d/%m/%Y')
    clock_text.config(text = string)
    clock_text.after(1000, time)

clock_text = tk.Label(top_bar, font=('calibri', 10, 'bold'), bg='black', fg='white')
clock_text.pack(side=tk.LEFT, padx=10)
time()

user_btn=tk.Label(top_bar,text="User",bg="black",fg="white",font=("Aptos Display",10,"bold"))
user_btn.pack(side=tk.RIGHT, padx=10)

Welcome_button = tk.Button(top_bar, text="Welcome", bg="gray", fg="white", font=("Aptos Display", 10,"bold"))
Welcome_button.pack(side=tk.RIGHT, padx=10)

left_panel = tk.Frame(root, bg="lightgray", width=200)
left_panel.pack(side=tk.LEFT, fill=tk.Y)

left_label = tk.Label(left_panel, text="Other Trains Status", bg="lightgray", font=("impact", 14))
left_label.pack(anchor="w", padx=10, pady=10)

train_names = ["Channai Express:-","156845476", "Superfast:- ","51684645", "Local:- ","5148641","Intercity:- ","1586488", "Rajdhani:- ","218486", "Shatabdi:- ","58184156"]

for train_name in train_names:
    tk.Label(left_panel, text=train_name, bg="lightgray", font=("Aptos Display", 10, "bold")).pack(anchor="w", padx=10, pady=5)

center_panel = tk.Frame(root, bg="gray")
center_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

info_label = tk.Label(center_panel, text="Information", font=("Aptos Display", 16, "bold"), bg="white")
info_label.pack(pady=10)

travel_date_label = tk.Label(center_panel, text="Traveling Date", font=("Aptos Display", 12), bg="white")
travel_date_label.pack(pady=10)

travel_date_entry = DateEntry(center_panel, font=("Aptos Display", 12), width=20, background='darkblue', foreground='white', borderwidth=2)
travel_date_entry.pack()

passenger_details_frame = tk.Frame(center_panel, bg="lightgray", relief=tk.RIDGE, borderwidth=4)
passenger_details_frame.pack(pady=20, fill=tk.X)

passenger_label = tk.Label(passenger_details_frame, text="Passenger Details", font=("Constantia", 20, "bold"), bg="white")
passenger_label.grid(row=0, column=0, columnspan=4, pady=10)

# Personal Details
full_name_label = tk.Label(passenger_details_frame, text="Full Name", font=("Aptos Display", 10), bg="white")
full_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
full_name_entry = tk.Entry(passenger_details_frame, font=("Aptos Display", 10), width=30)
full_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

age_label = tk.Label(passenger_details_frame, text="Age", font=("Aptos Display", 10), bg="white")
age_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")
age_entry = tk.Entry(passenger_details_frame, font=("Aptos Display", 10), width=5)
age_entry.grid(row=1, column=3, padx=10, pady=5, sticky="w")

gender_label = tk.Label(passenger_details_frame, text="Gender", font=("Aptos Display", 10), bg="white")
gender_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
gender_combobox = ttk.Combobox(passenger_details_frame, font=("Aptos Display", 10), values=["Male", "Female", "Other"])
gender_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

mobile_label = tk.Label(passenger_details_frame, text="Mobile Number", font=("Aptos Display", 10), bg="white")
mobile_label.grid(row=2, column=2, padx=10, pady=5, sticky="w")
mobile_entry = tk.Entry(passenger_details_frame, font=("Aptos Display", 10), width=15)
mobile_entry.grid(row=2, column=3, padx=10, pady=5, sticky="w")

email_label = tk.Label(passenger_details_frame, text="Email ID", font=("Aptos Display", 10), bg="white")
email_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
email_entry = tk.Entry(passenger_details_frame, font=("Aptos Display", 10), width=30)
email_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Journey Details
from_label = tk.Label(passenger_details_frame, text="From Station", font=("Aptos Display", 10), bg="white")
from_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
from_entry = tk.Entry(passenger_details_frame, font=("Aptos Display", 10), width=15)
from_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

to_label = tk.Label(passenger_details_frame, text="To Station", font=("Aptos Display", 10), bg="white")
to_label.grid(row=4, column=2, padx=10, pady=5, sticky="w")
to_entry = tk.Entry(passenger_details_frame, font=("Aptos Display", 10), width=15)
to_entry.grid(row=4, column=3, padx=10, pady=5, sticky="w")

class_label = tk.Label(passenger_details_frame, text="Class of Travel", font=("Aptos Display", 10), bg="white")
class_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
class_combobox = ttk.Combobox(passenger_details_frame, font=("Aptos Display", 10), values=["Sleeper", "AC 3-Tier", "AC 2-Tier", "AC 1-Tier", "General"])
class_combobox.grid(row=5, column=1, padx=10, pady=5, sticky="w")

train_label = tk.Label(passenger_details_frame, text="Train Number/Name", font=("Aptos Display", 10), bg="white")
train_label.grid(row=5, column=2, padx=10, pady=5, sticky="w")
train_entry = tk.Entry(passenger_details_frame, font=("Aptos Display", 10), width=15)
train_entry.grid(row=5, column=3, padx=10, pady=5, sticky="w")

quota_label = tk.Label(passenger_details_frame, text="Quota", font=("Aptos Display", 10), bg="white")
quota_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
quota_combobox = ttk.Combobox(passenger_details_frame, font=("Aptos Display", 10), values=["General", "Tatkal", "Ladies", "Senior Citizen"])
quota_combobox.grid(row=6, column=1, padx=10, pady=5, sticky="w")

# Passenger Preferences
seat_pref_label = tk.Label(passenger_details_frame, text="Seat Preference", font=("Aptos Display", 10), bg="white")
seat_pref_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
seat_pref_combobox = ttk.Combobox(passenger_details_frame, font=("Aptos Display", 10), values=["Lower", "Middle", "Upper", "Side Lower", "Side Upper"])
seat_pref_combobox.grid(row=7, column=1, padx=10, pady=5, sticky="w")

meal_pref_label = tk.Label(passenger_details_frame, text="Meal Preference", font=("Aptos Display", 10), bg="white")
meal_pref_label.grid(row=7, column=2, padx=10, pady=5, sticky="w")
meal_pref_combobox = ttk.Combobox(passenger_details_frame, font=("Aptos Display", 10), values=["Veg", "Non-Veg", "No Meal"])
meal_pref_combobox.grid(row=7, column=3, padx=10, pady=5, sticky="w")

coach_type_label = tk.Label(passenger_details_frame, text="Coach Type", font=("Aptos Display", 10), bg="white")
coach_type_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
coach_type_combobox = ttk.Combobox(passenger_details_frame, font=("Aptos Display", 10), values=["Window", "Aisle", "Any"])
coach_type_combobox.grid(row=8, column=1, padx=10, pady=5, sticky="w")

# Identity Proof
id_proof_label = tk.Label(passenger_details_frame, text="Identity Proof", font=("Aptos Display", 10), bg="white")
id_proof_label.grid(row=8, column=2, padx=10, pady=5, sticky="w")
id_proof_combobox = ttk.Combobox(passenger_details_frame, font=("Aptos Display", 10), values=["Aadhaar Card", "PAN Card", "Passport", "Voter ID", "Driving License", "Student ID"])
id_proof_combobox.grid(row=8, column=3, padx=10, pady=5, sticky="w")

# Reservation Type
reservation_type_var = tk.StringVar()
reservation_type_var.set("Reserve")

reserve_radio = tk.Radiobutton(passenger_details_frame, text="Reserve", font=("Aptos Display", 12, "bold"), bg="white", variable=reservation_type_var, value="Reserve")
reserve_radio.grid(row=9, column=0, padx=10, pady=10, sticky="w")

tatkal_radio = tk.Radiobutton(passenger_details_frame, text="Tatkal", font=("Aptos Display", 12, "bold"), bg="white", variable=reservation_type_var, value="Tatkal")
tatkal_radio.grid(row=9, column=1, padx=10, pady=10, sticky="w")

submit_button = tk.Button(passenger_details_frame, text="SUBMIT", bg="blue", fg="white", font=("Aptos Display", 10), command=lambda: generate_preview())
submit_button.grid(row=10, column=2, padx=10, pady=10, sticky="e")

preview_frame = tk.Frame(center_panel, bg="white", relief=tk.RIDGE, borderwidth=4)
preview_frame.pack(pady=20, fill=tk.BOTH, expand=True)



def generate_preview():
    for widget in preview_frame.winfo_children():
        widget.destroy()
    
    full_name = full_name_entry.get()
    age = age_entry.get()
    gender = gender_combobox.get()
    mobile = mobile_entry.get()
    email = email_entry.get()
    from_station = from_entry.get()
    to_station = to_entry.get()
    travel_date = travel_date_entry.get()
    travel_class = class_combobox.get()
    train_number = train_entry.get()
    quota = quota_combobox.get()
    seat_pref = seat_pref_combobox.get()
    meal_pref = meal_pref_combobox.get()
    coach_type = coach_type_combobox.get()
    id_proof = id_proof_combobox.get()
    reservation_type = reservation_type_var.get()
    
    preview_label = tk.Label(preview_frame, text=f"Full Name: {full_name}\nAge: {age}\nGender: {gender}\nMobile: {mobile}\nEmail: {email}\nFrom: {from_station}\nTo: {to_station}\nTravel Date: {travel_date}\nClass: {travel_class}\nTrain: {train_number}\nQuota: {quota}\nSeat Preference: {seat_pref}\nMeal Preference: {meal_pref}\nCoach Type: {coach_type}\nID Proof: {id_proof}\nReservation Type: {reservation_type}", font=("Aptos Display", 12), bg="white")
    preview_label.pack(pady=10)

    download_button = tk.Button(passenger_details_frame, text="Download as PDF", bg="red", fg="white", font=("Aptos Display", 10), command=lambda: download_pdf(full_name, age, gender, mobile, email, from_station, to_station, travel_date, travel_class, train_number, quota, seat_pref, meal_pref, coach_type, id_proof, reservation_type))
    download_button.grid(row=10, column=3, padx=10, pady=10, sticky="e")

def download_pdf(full_name, age, gender, mobile, email, from_station, to_station, travel_date, travel_class, train_number, quota, seat_pref, meal_pref, coach_type, id_proof, reservation_type):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Railway Reservation Details", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Full Name: {full_name}", ln=True)
    pdf.cell(200, 10, txt=f"Age: {age}", ln=True)
    pdf.cell(200, 10, txt=f"Gender: {gender}", ln=True)
    pdf.cell(200, 10, txt=f"Mobile: {mobile}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"From: {from_station}", ln=True)
    pdf.cell(200, 10, txt=f"To: {to_station}", ln=True)
    pdf.cell(200, 10, txt=f"Travel Date: {travel_date}", ln=True)
    pdf.cell(200, 10, txt=f"Class: {travel_class}", ln=True)
    pdf.cell(200, 10, txt=f"Train: {train_number}", ln=True)
    pdf.cell(200, 10, txt=f"Quota: {quota}", ln=True)
    pdf.cell(200, 10, txt=f"Seat Preference: {seat_pref}", ln=True)
    pdf.cell(200, 10, txt=f"Meal Preference: {meal_pref}", ln=True)
    pdf.cell(200, 10, txt=f"Coach Type: {coach_type}", ln=True)
    pdf.cell(200, 10, txt=f"ID Proof: {id_proof}", ln=True)
    pdf.cell(200, 10, txt=f"Reservation Type: {reservation_type}", ln=True)
    
    current_directory = os.getcwd()
    pdf.output(os.path.join(current_directory, "reservation_details.pdf"))


root.mainloop()