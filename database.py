# Database and Booking Management Module

import json
import os
from datetime import datetime
from config import AppConfig
import uuid

class BookingDatabase:
    """Handle booking storage and retrieval"""
    
    @staticmethod
    def generate_booking_id():
        """Generate unique booking reference"""
        return f"PNR{datetime.now().strftime('%Y%m%d')}{str(uuid.uuid4())[:8].upper()}"
    
    @staticmethod
    def save_booking(booking_data):
        """Save booking to file"""
        try:
            booking_id = BookingDatabase.generate_booking_id()
            booking_data['booking_id'] = booking_id
            booking_data['timestamp'] = datetime.now().isoformat()
            
            file_path = os.path.join(
                AppConfig.BOOKINGS_DIR,
                f"{booking_id}.json"
            )
            
            with open(file_path, 'w') as f:
                json.dump(booking_data, f, indent=4)
            
            return booking_id
        except Exception as e:
            print(f"Error saving booking: {e}")
            return None
    
    @staticmethod
    def load_booking(booking_id):
        """Load booking by ID"""
        try:
            file_path = os.path.join(AppConfig.BOOKINGS_DIR, f"{booking_id}.json")
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    return json.load(f)
            return None
        except Exception as e:
            print(f"Error loading booking: {e}")
            return None
    
    @staticmethod
    def get_user_bookings(username):
        """Get all bookings for a user"""
        try:
            bookings = []
            for filename in os.listdir(AppConfig.BOOKINGS_DIR):
                if filename.endswith('.json'):
                    file_path = os.path.join(AppConfig.BOOKINGS_DIR, filename)
                    with open(file_path, 'r') as f:
                        booking = json.load(f)
                        if booking.get('username') == username:
                            bookings.append(booking)
            return bookings
        except Exception as e:
            print(f"Error getting user bookings: {e}")
            return []
    
    @staticmethod
    def cancel_booking(booking_id):
        """Cancel booking and update status"""
        try:
            booking = BookingDatabase.load_booking(booking_id)
            if booking:
                booking['status'] = 'CANCELLED'
                booking['cancellation_time'] = datetime.now().isoformat()
                file_path = os.path.join(AppConfig.BOOKINGS_DIR, f"{booking_id}.json")
                with open(file_path, 'w') as f:
                    json.dump(booking, f, indent=4)
                return True
            return False
        except Exception as e:
            print(f"Error cancelling booking: {e}")
            return False
    
    @staticmethod
    def get_all_bookings():
        """Get all bookings (admin function)"""
        try:
            bookings = []
            for filename in os.listdir(AppConfig.BOOKINGS_DIR):
                if filename.endswith('.json'):
                    file_path = os.path.join(AppConfig.BOOKINGS_DIR, filename)
                    with open(file_path, 'r') as f:
                        bookings.append(json.load(f))
            return bookings
        except Exception as e:
            print(f"Error getting all bookings: {e}")
            return []

class UserDatabase:
    """Simple user authentication (replace with real authentication in production)"""
    
    USERS_FILE = os.path.join(AppConfig.DATA_DIR, "users.json")
    DEFAULT_USERS = {
        "admin": "admin123",
        "user": "password123",
        "test": "test123"
    }
    
    @staticmethod
    def initialize_users():
        """Initialize default users if file doesn't exist"""
        if not os.path.exists(UserDatabase.USERS_FILE):
            with open(UserDatabase.USERS_FILE, 'w') as f:
                json.dump(UserDatabase.DEFAULT_USERS, f, indent=4)
    
    @staticmethod
    def verify_user(username, password):
        """Verify user credentials"""
        UserDatabase.initialize_users()
        try:
            with open(UserDatabase.USERS_FILE, 'r') as f:
                users = json.load(f)
                return users.get(username) == password
        except:
            return False
    
    @staticmethod
    def register_user(username, password):
        """Register new user"""
        UserDatabase.initialize_users()
        try:
            with open(UserDatabase.USERS_FILE, 'r') as f:
                users = json.load(f)
            
            if username in users:
                return False, "User already exists"
            
            users[username] = password
            with open(UserDatabase.USERS_FILE, 'w') as f:
                json.dump(users, f, indent=4)
            return True, "User registered successfully"
        except Exception as e:
            return False, str(e)

# Initialize on import
UserDatabase.initialize_users()
