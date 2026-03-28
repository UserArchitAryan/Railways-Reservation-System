# Configuration and Constants for Railway Reservation System

import tkinter as tk
from tkinter import font
import os

class ScreenConfig:
    """Responsive screen configuration based on monitor resolution"""
    
    @staticmethod
    def get_screen_dimensions(root):
        """Get effective screen dimensions"""
        root.update_idletasks()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        dpi = root.winfo_fpixels('1i')
        
        return {
            'width': width,
            'height': height,
            'dpi': dpi,
            'scale': dpi / 96.0  # 96 is standard DPI
        }
    
    @staticmethod
    def get_scaled_font(font_name, base_size, style='', scale=1.0):
        """Get a font scaled according to screen resolution"""
        scaled_size = int(base_size * scale)
        if style:
            return font.Font(family=font_name, size=scaled_size, weight=style)
        return font.Font(family=font_name, size=scaled_size)

class Colors:
    """Application color scheme"""
    PRIMARY_DARK = "#1a1a1a"
    PRIMARY_BLUE = "#1E88E5"
    PRIMARY_GOLD = "#FFBB00"
    ACCENT_GRAY = "#E0E0E0"
    SUCCESS_GREEN = "#4CAF50"
    ERROR_RED = "#F44336"
    WARNING_ORANGE = "#FF9800"
    SECTION_BG = "#F5F5F5"
    BUTTON_BG = "#1E88E5"
    BUTTON_HOVER = "#1565C0"
    LABEL_TEXT = "#333333"
    BORDER_COLOR = "#CCCCCC"

class Fonts:
    """Font configurations"""
    TITLE_LARGE = ("Segoe UI", 20, "bold")
    TITLE_MEDIUM = ("Segoe UI", 16, "bold")
    HEADING = ("Segoe UI", 14, "bold")
    SUBHEADING = ("Segoe UI", 12, "bold")
    NORMAL = ("Segoe UI", 11)
    SMALL = ("Segoe UI", 9)
    MONO = ("Courier New", 10)

class TrainData:
    """Sample train data - connect to real database in production"""
    TRAINS = {
        "12345": {"name": "Mumbai Express", "route": "Mumbai - Delhi", "type": "Superfast"},
        "12346": {"name": "Chennai Express", "route": "Chennai - Delhi", "type": "Express"},
        "12347": {"name": "Rajdhani Express", "route": "Delhi - Mumbai", "type": "Premium"},
        "12348": {"name": "Shatabdi Express", "route": "Delhi - Agra", "type": "Express"},
        "12349": {"name": "Intercity Express", "route": "Delhi - Jaipur", "type": "Local"},
    }
    
    STATIONS = [
        "Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata",
        "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Indore",
        "Lucknow", "Chandigarh", "Goa", "Kerala", "Bhopal"
    ]
    
    CLASSES = ["Sleeper", "AC 3-Tier", "AC 2-Tier", "AC 1-Tier", "General"]
    
    QUOTAS = ["General", "Tatkal", "Ladies", "Senior Citizen", "PWD"]
    
    @staticmethod
    def get_base_fare(from_station, to_station, train_class):
        """Calculate base fare - simplified for demo"""
        base_fares = {
            "Sleeper": 500,
            "AC 3-Tier": 1000,
            "AC 2-Tier": 1500,
            "AC 1-Tier": 2500,
            "General": 250
        }
        return base_fares.get(train_class, 500)

class AppConfig:
    """Application configuration"""
    APP_NAME = "A.R.Y.A - Automated Railway Reservation System"
    VERSION = "2.0.0"
    AUTHOR = "Railway Reservation Team"
    MIN_WINDOW_WIDTH = 800
    MIN_WINDOW_HEIGHT = 600
    DEFAULT_WINDOW_WIDTH = 1350
    DEFAULT_WINDOW_HEIGHT = 700
    
    DATA_DIR = os.path.join(os.path.expanduser("~"), ".aryaRRS")
    BOOKINGS_DIR = os.path.join(DATA_DIR, "bookings")
    PDFS_DIR = os.path.join(DATA_DIR, "tickets")
    LOGS_DIR = os.path.join(DATA_DIR, "logs")
    
    @staticmethod
    def ensure_directories():
        """Ensure necessary directories exist"""
        for directory in [AppConfig.DATA_DIR, AppConfig.BOOKINGS_DIR, 
                         AppConfig.PDFS_DIR, AppConfig.LOGS_DIR]:
            os.makedirs(directory, exist_ok=True)

AppConfig.ensure_directories()
