# Enhanced Reservation System Main Panel

import tkinter as tk
from tkinter import ttk, messagebox
from time import strftime
from tkcalendar import DateEntry
import threading
from datetime import datetime

from config import AppConfig, Colors, Fonts, ScreenConfig, TrainData
from database import BookingDatabase
from ticket_generator import TicketPDFGenerator, FareCalculator
from ui_utils import (
    ResponsiveLabel, ResponsiveButton, ResponsiveEntry,
    ResponsiveFrame, SectionFrame, StyledCombobox, ScreenAdaptiveWindow
)

class ReservationSystemWindow:
    """Main reservation system window with responsive design"""
    
    def __init__(self, username="Guest"):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"{AppConfig.APP_NAME} - Reservation Panel")
        
        # Set responsive geometry
        width, height, x, y = ScreenAdaptiveWindow.get_window_geometry(self.root)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.minsize(1000, 700)
        
        # Configure style
        self.root.config(bg=Colors.PRIMARY_DARK)
        
        # Store original geometry for responsive reflow
        self.original_width = width
        self.original_height = height
        
        self.setup_ui()
        self.bind_resize()
    
    def setup_ui(self):
        """Setup main UI"""
        # Top navigation bar
        self.setup_top_bar()
        
        # Main content area
        content_frame = tk.Frame(self.root, bg=Colors.SECTION_BG)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(content_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tab 1: New Booking
        self.setup_booking_tab()
        
        # Tab 2: Booking History
        self.setup_history_tab()
        
        # Tab 3: My Bookings
        self.setup_my_bookings_tab()
        
        # Tab 4: About
        self.setup_about_tab()
    
    def setup_top_bar(self):
        """Setup top navigation bar"""
        top_frame = tk.Frame(self.root, bg=Colors.PRIMARY_DARK, height=60)
        top_frame.pack(side=tk.TOP, fill=tk.X)
        top_frame.pack_propagate(False)
        
        # Left side - Time and date
        left_frame = tk.Frame(top_frame, bg=Colors.PRIMARY_DARK)
        left_frame.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.clock_label = ResponsiveLabel(
            left_frame,
            text="",
            font_size=10,
            bg=Colors.PRIMARY_DARK,
            fg='white'
        )
        self.clock_label.pack()
        
        self.update_time()
        
        # Right side - User info
        right_frame = tk.Frame(top_frame, bg=Colors.PRIMARY_DARK)
        right_frame.pack(side=tk.RIGHT, padx=20, pady=10)
        
        ResponsiveLabel(
            right_frame,
            text=f"Logged in as: {self.username}",
            font_size=11,
            font_style="bold",
            bg=Colors.PRIMARY_DARK,
            fg=Colors.PRIMARY_GOLD
        ).pack(side=tk.LEFT, padx=10)
        
        logout_btn = ResponsiveButton(
            right_frame,
            text="Logout",
            font_size=10,
            on_click=self.logout,
            bg_color=Colors.ERROR_RED
        )
        logout_btn.pack(side=tk.LEFT, padx=10)
    
    def update_time(self):
        """Update time display"""
        time_string = strftime('%H:%M:%S %p | %A | %d/%m/%Y')
        self.clock_label.config(text=time_string)
        self.root.after(1000, self.update_time)
    
    def setup_booking_tab(self):
        """Setup new booking tab"""
        booking_frame = tk.Frame(self.notebook, bg=Colors.SECTION_BG)
        self.notebook.add(booking_frame, text="New Booking")
        
        # Create canvas with scrollbar for responsiveness
        canvas = tk.Canvas(booking_frame, bg=Colors.SECTION_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(booking_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=Colors.SECTION_BG)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Journey Details Section
        journey_frame = SectionFrame(scrollable_frame, text="Journey Details")
        journey_frame.pack(fill=tk.X, padx=15, pady=10)
        
        # From station
        ResponsiveLabel(
            journey_frame, text="From Station", font_size=10, 
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=0, column=0, padx=10, pady=8, sticky='w')
        
        self.from_station_combo = StyledCombobox(
            journey_frame, values=TrainData.STATIONS, width=25
        )
        self.from_station_combo.grid(row=0, column=1, padx=10, pady=8)
        
        # To station
        ResponsiveLabel(
            journey_frame, text="To Station", font_size=10,
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=0, column=2, padx=10, pady=8, sticky='w')
        
        self.to_station_combo = StyledCombobox(
            journey_frame, values=TrainData.STATIONS, width=25
        )
        self.to_station_combo.grid(row=0, column=3, padx=10, pady=8)
        
        # Travel date
        ResponsiveLabel(
            journey_frame, text="Travel Date", font_size=10,
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=1, column=0, padx=10, pady=8, sticky='w')
        
        self.travel_date_entry = DateEntry(
            journey_frame, font=Fonts.NORMAL, width=25,
            background=Colors.PRIMARY_BLUE, foreground='white', borderwidth=2
        )
        self.travel_date_entry.grid(row=1, column=1, padx=10, pady=8)
        
        # Passenger Details Section
        passenger_frame = SectionFrame(scrollable_frame, text="Passenger Details")
        passenger_frame.pack(fill=tk.X, padx=15, pady=10)
        
        # Full name
        ResponsiveLabel(
            passenger_frame, text="Full Name", font_size=10,
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=0, column=0, padx=10, pady=8, sticky='w')
        
        self.full_name_entry = ResponsiveEntry(passenger_frame, font_size=10)
        self.full_name_entry.grid(row=0, column=1, padx=10, pady=8, sticky='ew')
        
        # Age
        ResponsiveLabel(
            passenger_frame, text="Age", font_size=10,
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=0, column=2, padx=10, pady=8, sticky='w')
        
        self.age_entry = ResponsiveEntry(passenger_frame, font_size=10)
        self.age_entry.grid(row=0, column=3, padx=10, pady=8, sticky='ew')
        
        # Gender
        ResponsiveLabel(
            passenger_frame, text="Gender", font_size=10,
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=1, column=0, padx=10, pady=8, sticky='w')
        
        self.gender_combo = StyledCombobox(
            passenger_frame, values=["Male", "Female", "Other"], width=25
        )
        self.gender_combo.grid(row=1, column=1, padx=10, pady=8)
        
        # Email
        ResponsiveLabel(
            passenger_frame, text="Email", font_size=10,
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=1, column=2, padx=10, pady=8, sticky='w')
        
        self.email_entry = ResponsiveEntry(passenger_frame, font_size=10)
        self.email_entry.grid(row=1, column=3, padx=10, pady=8, sticky='ew')
        
        # Mobile
        ResponsiveLabel(
            passenger_frame, text="Mobile", font_size=10,
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=2, column=0, padx=10, pady=8, sticky='w')
        
        self.mobile_entry = ResponsiveEntry(passenger_frame, font_size=10)
        self.mobile_entry.grid(row=2, column=1, padx=10, pady=8, sticky='ew')
        
        # Travel & Preferences Section
        travel_frame = SectionFrame(scrollable_frame, text="Travel & Preferences")
        travel_frame.pack(fill=tk.X, padx=15, pady=10)
        
        # Class
        ResponsiveLabel(
            travel_frame, text="Class", font_size=10,
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=0, column=0, padx=10, pady=8, sticky='w')
        
        self.class_combo = StyledCombobox(
            travel_frame, values=TrainData.CLASSES, width=25
        )
        self.class_combo.grid(row=0, column=1, padx=10, pady=8)
        self.class_combo.bind('<<ComboboxSelected>>', self.update_fare_estimate)
        
        # Quota
        ResponsiveLabel(
            travel_frame, text="Quota", font_size=10,
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=0, column=2, padx=10, pady=8, sticky='w')
        
        self.quota_combo = StyledCombobox(
            travel_frame, values=TrainData.QUOTAS, width=25
        )
        self.quota_combo.grid(row=0, column=3, padx=10, pady=8)
        
        # Seat preference
        ResponsiveLabel(
            travel_frame, text="Seat Preference", font_size=10,
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=1, column=0, padx=10, pady=8, sticky='w')
        
        self.seat_pref_combo = StyledCombobox(
            travel_frame, values=["Lower", "Middle", "Upper", "Side Lower", "Side Upper"], width=25
        )
        self.seat_pref_combo.grid(row=1, column=1, padx=10, pady=8)
        
        # Meal preference
        ResponsiveLabel(
            travel_frame, text="Meal", font_size=10,
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=1, column=2, padx=10, pady=8, sticky='w')
        
        self.meal_combo = StyledCombobox(
            travel_frame, values=["Veg", "Non-Veg", "No Meal"], width=25
        )
        self.meal_combo.grid(row=1, column=3, padx=10, pady=8)
        
        # ID Proof
        ResponsiveLabel(
            travel_frame, text="ID Proof", font_size=10,
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=2, column=0, padx=10, pady=8, sticky='w')
        
        self.id_proof_combo = StyledCombobox(
            travel_frame, values=["Aadhaar", "PAN", "Passport", "Voter ID", "Driving License"], width=25
        )
        self.id_proof_combo.grid(row=2, column=1, padx=10, pady=8)
        
        # Fare estimate
        ResponsiveLabel(
            travel_frame, text="Estimated Fare", font_size=10,
            bg=Colors.SECTION_BG, fg=Colors.LABEL_TEXT
        ).grid(row=2, column=2, padx=10, pady=8, sticky='w')
        
        self.fare_label = ResponsiveLabel(
            travel_frame, text="Rs. 0", font_size=10, font_style="bold",
            bg=Colors.SECTION_BG, fg=Colors.SUCCESS_GREEN
        )
        self.fare_label.grid(row=2, column=3, padx=10, pady=8)
        
        # Buttons
        button_frame = tk.Frame(scrollable_frame, bg=Colors.SECTION_BG)
        button_frame.pack(fill=tk.X, padx=15, pady=20)
        
        search_btn = ResponsiveButton(
            button_frame, text="Search Trains", font_size=11,
            on_click=self.search_trains, bg_color=Colors.PRIMARY_BLUE
        )
        search_btn.pack(side=tk.LEFT, padx=10)
        
        book_btn = ResponsiveButton(
            button_frame, text="Book Ticket", font_size=11,
            on_click=self.book_ticket, bg_color=Colors.SUCCESS_GREEN
        )
        book_btn.pack(side=tk.LEFT, padx=10)
        
        clear_btn = ResponsiveButton(
            button_frame, text="Clear Form", font_size=11,
            on_click=self.clear_form, bg_color=Colors.WARNING_ORANGE
        )
        clear_btn.pack(side=tk.LEFT, padx=10)
        
        # Configure column weights for responsiveness
        for i in range(4):
            passenger_frame.grid_columnconfigure(i, weight=1)
            travel_frame.grid_columnconfigure(i, weight=1)
    
    def setup_history_tab(self):
        """Setup booking history tab"""
        history_frame = tk.Frame(self.notebook, bg=Colors.SECTION_BG)
        self.notebook.add(history_frame, text="Booking History")
        
        # Create treeview
        columns = ("Date", "From", "To", "Class", "Status", "Fare")
        self.history_tree = ttk.Treeview(
            history_frame, columns=columns, height=15, show="headings"
        )
        
        for col in columns:
            self.history_tree.column(col, width=100)
            self.history_tree.heading(col, text=col)
        
        scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=self.history_tree.yview)
        self.history_tree.configure(yscroll=scrollbar.set)
        
        self.history_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Load history button
        reload_btn = ResponsiveButton(
            history_frame, text="Reload History", font_size=10,
            on_click=self.load_booking_history, bg_color=Colors.PRIMARY_BLUE
        )
        reload_btn.pack(pady=10)
    
    def setup_my_bookings_tab(self):
        """Setup my bookings tab"""
        bookings_frame = tk.Frame(self.notebook, bg=Colors.SECTION_BG)
        self.notebook.add(bookings_frame, text="My Bookings")
        
        # Info frame
        info_frame = SectionFrame(bookings_frame, text="Your Bookings")
        info_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        self.bookings_text = tk.Text(
            info_frame, height=20, width=80, font=Fonts.NORMAL,
            bg='white', fg=Colors.LABEL_TEXT, relief=tk.FLAT, bd=2
        )
        self.bookings_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Buttons
        button_frame = tk.Frame(bookings_frame, bg=Colors.SECTION_BG)
        button_frame.pack(fill=tk.X, padx=15, pady=10)
        
        refresh_btn = ResponsiveButton(
            button_frame, text="Refresh Bookings", font_size=10,
            on_click=self.load_my_bookings, bg_color=Colors.PRIMARY_BLUE
        )
        refresh_btn.pack(side=tk.LEFT, padx=5)
        
        download_btn = ResponsiveButton(
            button_frame, text="Download Ticket", font_size=10,
            on_click=self.download_ticket, bg_color=Colors.SUCCESS_GREEN
        )
        download_btn.pack(side=tk.LEFT, padx=5)
        
        cancel_btn = ResponsiveButton(
            button_frame, text="Cancel Booking", font_size=10,
            on_click=self.cancel_booking_dialog, bg_color=Colors.ERROR_RED
        )
        cancel_btn.pack(side=tk.LEFT, padx=5)
    
    def setup_about_tab(self):
        """Setup about tab"""
        about_frame = tk.Frame(self.notebook, bg=Colors.SECTION_BG)
        self.notebook.add(about_frame, text="About")
        
        content = tk.Frame(about_frame, bg=Colors.SECTION_BG)
        content.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Title
        title = ResponsiveLabel(
            content, text="A.R.Y.A", font_size=28, font_style="bold",
            bg=Colors.SECTION_BG, fg=Colors.PRIMARY_BLUE
        )
        title.pack(pady=20)
        
        # Description
        description = tk.Text(
            content, height=12, width=70, font=Fonts.NORMAL,
            bg='white', fg=Colors.LABEL_TEXT, relief=tk.FLAT, bd=2
        )
        description.pack(fill=tk.BOTH, expand=True)
        
        about_text = f"""
Automated Railway Reservation System (A.R.Y.A)
Version: {AppConfig.VERSION}

A modern, production-ready railway reservation system with:

• Responsive design - Auto-adjusts to any screen size
• Professional QR code-based tickets with detailed formatting
• Real-time booking management and history
• Secure user authentication
• Multiple booking quotas and preferences
• Fare calculation and estimation
• PDF generation with booking details

Features:
- Book railway tickets with multiple options
- View booking history and past reservations
- Cancel bookings with automatic refund calculation
- Download tickets as professional PDF documents
- Save booking preferences for faster booking
- Real-time train availability checking

{AppConfig.AUTHOR}
© 2026 All rights reserved.

For more information and support, please visit our website.
        """
        
        description.insert(1.0, about_text)
        description.config(state=tk.DISABLED)
    
    def update_fare_estimate(self, event=None):
        """Update fare estimate"""
        try:
            from_station = self.from_station_combo.get()
            to_station = self.to_station_combo.get()
            travel_class = self.class_combo.get()
            
            if from_station and to_station and travel_class:
                fare = FareCalculator.calculate_fare(from_station, to_station, travel_class)
                self.fare_label.config(text=f"Rs. {fare:.2f}")
        except:
            pass
    
    def search_trains(self):
        """Search available trains"""
        messagebox.showinfo(
            "Search Results",
            "Available trains:\n\n" + "\n".join([f"{k}: {v['name']}" for k, v in TrainData.TRAINS.items()])
        )
    
    def book_ticket(self):
        """Book a ticket"""
        # Validate inputs
        if not all([
            self.full_name_entry.get(),
            self.age_entry.get(),
            self.from_station_combo.get(),
            self.to_station_combo.get(),
            self.class_combo.get()
        ]):
            messagebox.showerror("Validation Error", "Please fill all required fields")
            return
        
        # Create booking data
        booking_data = {
            'username': self.username,
            'full_name': self.full_name_entry.get(),
            'age': self.age_entry.get(),
            'gender': self.gender_combo.get(),
            'email': self.email_entry.get(),
            'mobile': self.mobile_entry.get(),
            'from_station': self.from_station_combo.get(),
            'to_station': self.to_station_combo.get(),
            'travel_date': str(self.travel_date_entry.get()),
            'travel_class': self.class_combo.get(),
            'quota': self.quota_combo.get(),
            'seat_pref': self.seat_pref_combo.get(),
            'meal_pref': self.meal_combo.get(),
            'id_proof': self.id_proof_combo.get(),
            'train_number': '12345',
            'reservation_type': 'Reserve',
            'status': 'CONFIRMED',
            'base_fare': FareCalculator.calculate_fare(
                self.from_station_combo.get(),
                self.to_station_combo.get(),
                self.class_combo.get()
            )
        }
        
        # Save booking
        booking_id = BookingDatabase.save_booking(booking_data)
        if booking_id:
            # Generate PDF
            pdf_path = TicketPDFGenerator.generate_ticket_pdf(booking_data)
            
            messagebox.showinfo(
                "Booking Confirmed",
                f"Your booking is confirmed!\n\nBooking ID: {booking_id}\n"
                f"Ticket saved at: {pdf_path}\n\n"
                f"Please keep this reference number for future use."
            )
            
            self.clear_form()
            self.load_my_bookings()
        else:
            messagebox.showerror("Booking Failed", "Could not save booking. Please try again.")
    
    def clear_form(self):
        """Clear booking form"""
        self.full_name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        self.from_station_combo.set('')
        self.to_station_combo.set('')
        self.gender_combo.set('')
        self.class_combo.set('')
        self.quota_combo.set('')
        self.seat_pref_combo.set('')
        self.meal_combo.set('')
        self.id_proof_combo.set('')
    
    def load_booking_history(self):
        """Load booking history"""
        bookings = BookingDatabase.get_all_bookings()
        
        # Clear tree
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)
        
        # Add bookings
        for booking in bookings[:10]:  # Show last 10
            self.history_tree.insert(
                '', 'end',
                values=(
                    booking.get('travel_date', 'N/A'),
                    booking.get('from_station', 'N/A'),
                    booking.get('to_station', 'N/A'),
                    booking.get('travel_class', 'N/A'),
                    booking.get('status', 'N/A'),
                    f"Rs. {booking.get('base_fare', 0):.2f}"
                )
            )
    
    def load_my_bookings(self):
        """Load user's bookings"""
        self.bookings_text.config(state=tk.NORMAL)
        self.bookings_text.delete(1.0, tk.END)
        
        bookings = BookingDatabase.get_user_bookings(self.username)
        
        if not bookings:
            self.bookings_text.insert(tk.END, "No bookings found.")
        else:
            for booking in bookings:
                booking_info = f"""
Booking ID: {booking.get('booking_id', 'N/A')}
Name: {booking.get('full_name', 'N/A')}
From: {booking.get('from_station', 'N/A')} → To: {booking.get('to_station', 'N/A')}
Date: {booking.get('travel_date', 'N/A')}
Class: {booking.get('travel_class', 'N/A')}
Status: {booking.get('status', 'N/A')}
Fare: Rs. {booking.get('base_fare', 0):.2f}
---\n"""
                self.bookings_text.insert(tk.END, booking_info)
        
        self.bookings_text.config(state=tk.DISABLED)
    
    def download_ticket(self):
        """Download ticket as PDF"""
        messagebox.showinfo(
            "Download",
            "Tickets are automatically saved in:\n" + AppConfig.PDFS_DIR
        )
    
    def cancel_booking_dialog(self):
        """Cancel booking dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Cancel Booking")
        dialog.geometry("400x150")
        
        frame = tk.Frame(dialog, bg=Colors.PRIMARY_DARK)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        ResponsiveLabel(
            frame, text="Enter Booking ID to cancel:",
            bg=Colors.PRIMARY_DARK, fg='white'
        ).pack(pady=10)
        
        entry = ResponsiveEntry(frame)
        entry.pack(fill=tk.X, pady=10)
        
        def cancel():
            booking_id = entry.get().strip()
            if booking_id:
                if BookingDatabase.cancel_booking(booking_id):
                    messagebox.showinfo("Success", f"Booking {booking_id} cancelled successfully")
                    dialog.destroy()
                else:
                    messagebox.showerror("Error", "Booking not found")
        
        ResponsiveButton(
            frame, text="Cancel Booking", on_click=cancel, bg_color=Colors.ERROR_RED
        ).pack(fill=tk.X, pady=10)
    
    def bind_resize(self):
        """Bind window resize event for responsive design"""
        def on_resize(event):
            pass  # Responsive design handled by tkinter pack/grid
        
        self.root.bind('<Configure>', on_resize)
    
    def logout(self):
        """Logout and return to login"""
        result = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if result:
            self.root.destroy()
            from login_enhanced import EnhancedLoginWindow
            app = EnhancedLoginWindow()
            app.run()
    
    def run(self):
        """Run main window"""
        self.load_booking_history()
        self.load_my_bookings()
        self.root.mainloop()

def main():
    """Main entry point"""
    app = ReservationSystemWindow("Guest")
    app.run()

if __name__ == "__main__":
    main()
