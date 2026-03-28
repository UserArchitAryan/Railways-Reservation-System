# Enhanced Login Module with Validation

import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from config import AppConfig, Colors, Fonts
from database import UserDatabase
from ui_utils import (
    ResponsiveLabel, ResponsiveButton, ResponsiveEntry, 
    ScreenAdaptiveWindow, InputField
)

class EnhancedLoginWindow:
    """Modern login window with validation and responsive design"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(f"{AppConfig.APP_NAME} - Login")
        
        # Set responsive geometry
        width, height, x, y = ScreenAdaptiveWindow.get_window_geometry(
            self.root, 
            default_width=500, 
            default_height=600
        )
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.resizable(True, True)
        self.root.minsize(400, 500)
        
        # Configure background
        self.root.config(bg=Colors.PRIMARY_DARK)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup login UI"""
        # Main container
        main_frame = tk.Frame(self.root, bg=Colors.PRIMARY_DARK)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header frame
        header_frame = tk.Frame(main_frame, bg=Colors.PRIMARY_GOLD, height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Title in header
        title_label = ResponsiveLabel(
            header_frame,
            text="A.R.Y.A",
            font_size=36,
            font_style="bold",
            bg=Colors.PRIMARY_GOLD,
            fg=Colors.PRIMARY_DARK
        )
        title_label.pack(pady=15)
        
        # Content frame
        content_frame = tk.Frame(main_frame, bg=Colors.PRIMARY_DARK)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        # Introduction text
        intro_label = ResponsiveLabel(
            content_frame,
            text="Welcome to Railway Reservation System",
            font_size=14,
            font_style="bold",
            bg=Colors.PRIMARY_DARK,
            fg='white'
        )
        intro_label.pack(pady=(0, 10))
        
        subtitle_label = ResponsiveLabel(
            content_frame,
            text="Sign in to your account to continue",
            font_size=11,
            bg=Colors.PRIMARY_DARK,
            fg=Colors.ACCENT_GRAY
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Input fields frame
        input_frame = tk.Frame(content_frame, bg=Colors.PRIMARY_DARK)
        input_frame.pack(fill=tk.X, pady=20)
        
        # Username
        username_label = ResponsiveLabel(
            input_frame,
            text="Username",
            font_size=11,
            font_style="bold",
            bg=Colors.PRIMARY_DARK,
            fg='white'
        )
        username_label.pack(anchor='w', pady=(10, 5))
        
        self.username_entry = ResponsiveEntry(input_frame, font_size=11)
        self.username_entry.pack(fill=tk.X, pady=(0, 20))
        self.username_entry.config(bg='white', insertbackground=Colors.PRIMARY_BLUE)
        
        # Password
        password_label = ResponsiveLabel(
            input_frame,
            text="Password",
            font_size=11,
            font_style="bold",
            bg=Colors.PRIMARY_DARK,
            fg='white'
        )
        password_label.pack(anchor='w', pady=(0, 5))
        
        self.password_entry = ResponsiveEntry(input_frame, font_size=11)
        self.password_entry.pack(fill=tk.X, pady=(0, 20))
        self.password_entry.config(show="•", bg='white', insertbackground=Colors.PRIMARY_BLUE)
        
        # Remember me
        self.remember_var = tk.BooleanVar()
        remember_check = tk.Checkbutton(
            input_frame,
            text="Remember me",
            variable=self.remember_var,
            font=Fonts.SMALL,
            bg=Colors.PRIMARY_DARK,
            fg='white',
            selectcolor=Colors.PRIMARY_DARK,
            activebackground=Colors.PRIMARY_DARK,
            activeforeground='white'
        )
        remember_check.pack(anchor='w', pady=(0, 30))
        
        # Buttons frame
        button_frame = tk.Frame(input_frame, bg=Colors.PRIMARY_DARK)
        button_frame.pack(fill=tk.X, pady=20)
        
        # Login button
        login_button = ResponsiveButton(
            button_frame,
            text="Sign In",
            font_size=12,
            on_click=self.handle_login,
            bg_color=Colors.PRIMARY_BLUE
        )
        login_button.pack(fill=tk.X, pady=10)
        
        # Register button
        register_button = ResponsiveButton(
            button_frame,
            text="Create Account",
            font_size=12,
            on_click=self.show_register_window,
            bg_color=Colors.SUCCESS_GREEN
        )
        register_button.pack(fill=tk.X, pady=5)
        
        # Guest button
        guest_button = ResponsiveButton(
            button_frame,
            text="Continue as Guest",
            font_size=12,
            on_click=self.handle_guest_login,
            bg_color=Colors.WARNING_ORANGE
        )
        guest_button.pack(fill=tk.X, pady=5)
        
        # Exit button
        exit_button = ResponsiveButton(
            button_frame,
            text="Exit",
            font_size=12,
            on_click=self.root.quit,
            bg_color=Colors.ERROR_RED
        )
        exit_button.pack(fill=tk.X, pady=5)
        
        # Bind Enter key for login
        self.password_entry.bind('<Return>', lambda e: self.handle_login())
        
        # Credentials hint for demo
        hint_frame = tk.Frame(content_frame, bg=Colors.PRIMARY_DARK)
        hint_frame.pack(fill=tk.X, pady=(40, 0), padx=20)
        
        hint_label = ResponsiveLabel(
            hint_frame,
            text="Demo Credentials: admin/admin123, user/password123",
            font_size=9,
            bg=Colors.PRIMARY_DARK,
            fg=Colors.WARNING_ORANGE
        )
        hint_label.pack()
    
    def handle_login(self):
        """Handle login attempt"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Validation Error", "Please enter both username and password")
            return
        
        if UserDatabase.verify_user(username, password):
            messagebox.showinfo("Login Successful", f"Welcome back, {username}!")
            self.root.destroy()
            self.launch_main_app(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            self.password_entry.delete(0, tk.END)
    
    def handle_guest_login(self):
        """Handle guest login"""
        result = messagebox.askyesno(
            "Guest Mode",
            "Continue as guest? You won't be able to save your bookings."
        )
        if result:
            self.root.destroy()
            self.launch_main_app("Guest")
    
    def show_register_window(self):
        """Show registration window"""
        register_window = tk.Toplevel(self.root)
        register_window.title("Create Account")
        register_window.geometry("400x300")
        
        # Center window
        register_window.transient(self.root)
        register_window.grab_set()
        
        # Content
        frame = tk.Frame(register_window, bg=Colors.PRIMARY_DARK)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title = ResponsiveLabel(
            frame,
            text="Create New Account",
            font_size=14,
            font_style="bold",
            bg=Colors.PRIMARY_DARK,
            fg='white'
        )
        title.pack(pady=20)
        
        # Username
        username_label = ResponsiveLabel(
            frame,
            text="Username",
            font_size=11,
            bg=Colors.PRIMARY_DARK,
            fg='white'
        )
        username_label.pack(anchor='w', pady=(10, 5))
        
        reg_username = ResponsiveEntry(frame, font_size=11)
        reg_username.pack(fill=tk.X, pady=(0, 15))
        reg_username.config(bg='white')
        
        # Password
        password_label = ResponsiveLabel(
            frame,
            text="Password",
            font_size=11,
            bg=Colors.PRIMARY_DARK,
            fg='white'
        )
        password_label.pack(anchor='w', pady=(0, 5))
        
        reg_password = ResponsiveEntry(frame, font_size=11)
        reg_password.pack(fill=tk.X, pady=(0, 15))
        reg_password.config(show="•", bg='white')
        
        # Confirm Password
        confirm_label = ResponsiveLabel(
            frame,
            text="Confirm Password",
            font_size=11,
            bg=Colors.PRIMARY_DARK,
            fg='white'
        )
        confirm_label.pack(anchor='w', pady=(0, 5))
        
        reg_confirm = ResponsiveEntry(frame, font_size=11)
        reg_confirm.pack(fill=tk.X, pady=(0, 20))
        reg_confirm.config(show="•", bg='white')
        
        def register_user():
            username = reg_username.get().strip()
            password = reg_password.get()
            confirm = reg_confirm.get()
            
            if not username or not password or not confirm:
                messagebox.showerror("Error", "All fields are required")
                return
            
            if password != confirm:
                messagebox.showerror("Error", "Passwords do not match")
                return
            
            if len(password) < 6:
                messagebox.showerror("Error", "Password must be at least 6 characters")
                return
            
            success, message = UserDatabase.register_user(username, password)
            if success:
                messagebox.showinfo("Success", message)
                register_window.destroy()
            else:
                messagebox.showerror("Error", message)
        
        button_frame = tk.Frame(frame, bg=Colors.PRIMARY_DARK)
        button_frame.pack(fill=tk.X, pady=20)
        
        register_btn = ResponsiveButton(
            button_frame,
            text="Create Account",
            on_click=register_user,
            bg_color=Colors.SUCCESS_GREEN
        )
        register_btn.pack(fill=tk.X, pady=5)
        
        cancel_btn = ResponsiveButton(
            button_frame,
            text="Cancel",
            on_click=register_window.destroy,
            bg_color=Colors.ERROR_RED
        )
        cancel_btn.pack(fill=tk.X, pady=5)
    
    def launch_main_app(self, username):
        """Launch main application"""
        from reservation_panel import ReservationSystemWindow
        main_window = ReservationSystemWindow(username)
        main_window.run()
    
    def run(self):
        """Run login window"""
        self.root.mainloop()

def main():
    """Main entry point"""
    app = EnhancedLoginWindow()
    app.run()

if __name__ == "__main__":
    main()
