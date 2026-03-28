# Application Launcher with Splash Screen

import tkinter as tk
from tkinter import ttk
import threading
import time
import os
from config import AppConfig, Colors, Fonts, ScreenConfig
from ui_utils import ResponsiveLabel, ResponsiveButton, ScreenAdaptiveWindow

class SplashScreen:
    """Modern splash screen for application startup"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("A.R.Y.A - Loading")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Center window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 600) // 2
        y = (screen_height - 400) // 2
        self.root.geometry(f"600x400+{x}+{y}")
        
        # Remove window decorations for clean look
        self.root.config(bg=Colors.PRIMARY_DARK)
        
        # Main container
        main_frame = tk.Frame(self.root, bg=Colors.PRIMARY_DARK)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Logo/Title
        title_label = tk.Label(
            main_frame,
            text="A.R.Y.A",
            font=("Segoe UI", 48, "bold"),
            bg=Colors.PRIMARY_DARK,
            fg=Colors.PRIMARY_GOLD
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Automated Railway Reservation System",
            font=("Segoe UI", 14),
            bg=Colors.PRIMARY_DARK,
            fg=Colors.ACCENT_GRAY
        )
        subtitle_label.pack(pady=5)
        
        # Version
        version_label = tk.Label(
            main_frame,
            text=f"Version {AppConfig.VERSION}",
            font=("Segoe UI", 10),
            bg=Colors.PRIMARY_DARK,
            fg=Colors.ACCENT_GRAY
        )
        version_label.pack()
        
        # Progress area
        progress_frame = tk.Frame(main_frame, bg=Colors.PRIMARY_DARK)
        progress_frame.pack(pady=40, fill=tk.X)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            progress_frame,
            mode='indeterminate',
            length=300,
            style='TProgressbar'
        )
        self.progress.pack(pady=10)
        
        # Status label
        self.status_label = tk.Label(
            progress_frame,
            text="Initializing...",
            font=("Segoe UI", 11),
            bg=Colors.PRIMARY_DARK,
            fg=Colors.PRIMARY_BLUE
        )
        self.status_label.pack()
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="© 2026 Railway Reservation System. All rights reserved.",
            font=("Segoe UI", 8),
            bg=Colors.PRIMARY_DARK,
            fg=Colors.ACCENT_GRAY
        )
        footer_label.pack(side=tk.BOTTOM, pady=20)
        
        self.progress.start()
    
    def update_status(self, message):
        """Update status message"""
        self.status_label.config(text=message)
        self.root.update()
    
    def close(self):
        """Close splash screen"""
        self.progress.stop()
        self.root.destroy()
    
    def show(self):
        """Show splash screen"""
        return self.root

class ApplicationLauncher:
    """Main application launcher"""
    
    def __init__(self):
        self.splash = None
        self.main_window = None
    
    def initialize(self):
        """Initialize application"""
        self.splash = SplashScreen()
        
        # Simulate initialization with status updates
        initialization_steps = [
            ("Initializing databases...", 0.3),
            ("Loading configuration...", 0.3),
            ("Preparing user interface...", 0.4)
        ]
        
        for step, delay in initialization_steps:
            self.splash.update_status(step)
            time.sleep(delay)
        
        self.splash.update_status("Ready!")
        time.sleep(0.5)
        self.splash.close()
    
    def launch_login(self):
        """Launch login window"""
        from login_enhanced import EnhancedLoginWindow
        window = EnhancedLoginWindow()
        window.run()
    
    def run(self):
        """Run launcher"""
        self.initialize()
        self.launch_login()

def main():
    """Main entry point"""
    try:
        launcher = ApplicationLauncher()
        launcher.run()
    except Exception as e:
        print(f"Error launching application: {e}")
        raise

if __name__ == "__main__":
    main()
