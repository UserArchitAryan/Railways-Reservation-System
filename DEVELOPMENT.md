# DEVELOPMENT Guide - A.R.Y.A Railway Reservation System

## Overview for Developers

This guide helps developers understand the codebase, extend features, and contribute to the project.

## Project Architecture

### Modular Design

```
Core Modules:
├── Launcher (launcher.py)
│   └── Handles app initialization and splash screen
├── Authentication (login_enhanced.py)
│   └── User login, registration, credential management
├── Main UI (reservation_panel.py)
│   └── Multi-tab interface with all features
├── Data Layer (database.py)
│   └── File-based storage, user management
├── PDF Generation (ticket_generator.py)
│   └── QR codes and professional PDF creation
└── Utilities
    ├── UI Components (ui_utils.py)
    ├── Configuration (config.py)
    └── Constants and styling
```

## Module Descriptions

### config.py
**Purpose**: Centralized configuration and constants

```python
# Screen configuration for responsive design
class ScreenConfig:
    @staticmethod get_screen_dimensions(root)
    @staticmethod get_scaled_font(font_name, size, style, scale)

# Color scheme
class Colors:
    PRIMARY_DARK = "#1a1a1a"
    # ... more colors

# Font definitions
class Fonts:
    TITLE_LARGE = ("Segoe UI", 20, "bold")
    # ... more fonts

# Train and system data
class TrainData:
    TRAINS = {...}
    STATIONS = [...]

# Application constants
class AppConfig:
    APP_NAME = "A.R.Y.A"
    VERSION = "2.0.0"
    DATA_DIR = os.path.expanduser("~/.aryaRRS")
```

**Key Features**:
- Responsive screen configuration
- Centralized color scheme
- Train and station data
- Application metadata

**Extension Points**:
- Add new trains to `TrainData.TRAINS`
- Modify color scheme in `Colors` class
- Update app version in `AppConfig`

### database.py
**Purpose**: Data persistence layer

**Classes**:
```python
class BookingDatabase:
    @staticmethod generate_booking_id()
    @staticmethod save_booking(booking_data)
    @staticmethod load_booking(booking_id)
    @staticmethod get_user_bookings(username)
    @staticmethod cancel_booking(booking_id)
    @staticmethod get_all_bookings()

class UserDatabase:
    @staticmethod initialize_users()
    @staticmethod verify_user(username, password)
    @staticmethod register_user(username, password)
```

**Data Format**:
- JSON files in `~/.aryaRRS/bookings/`
- User data in `~/.aryaRRS/users.json`

**Extension Points**:
- Replace with SQL database
- Add encryption for passwords
- Implement remote API calls
- Add data validation layer

### ticket_generator.py
**Purpose**: PDF generation and fare calculation

**Classes**:
```python
class TicketPDFGenerator:
    @staticmethod generate_ticket_pdf(booking_data)
    @staticmethod _generate_qr_code(booking_data)

class FareCalculator:
    @staticmethod calculate_fare(from, to, class)
    @staticmethod estimate_distance(from, to)
```

**File Output**: PDF files in `~/.aryaRRS/tickets/`

**Extension Points**:
- Customize PDF template
- Add email delivery
- Implement actual distance calculation
- Add GST/taxes dynamically
- Support multiple currencies

### ui_utils.py
**Purpose**: Responsive UI components

**Classes**:
```python
class ResponsiveFrame(tk.Frame)
class ResponsiveLabel(tk.Label)
class ResponsiveEntry(tk.Entry)
class ResponsiveButton(tk.Button)
class StyledCombobox(ttk.Combobox)
class SectionFrame(tk.LabelFrame)
class InputField  # Wrapper
class ScreenAdaptiveWindow  # Mixin
class PageIndicator  # Multi-page support
```

**Extension Points**:
- Add new custom widgets
- Modify hover effects
- Add animations
- Implement dark/light theme toggle

### launcher.py
**Purpose**: Application initialization

**Classes**:
```python
class SplashScreen:
    # Modern splash with progress
    
class ApplicationLauncher:
    def initialize()
    def launch_login()
    def run()
```

**Features**:
- Splash screen with animation
- Initialization sequence
- Error handling

**Extension Points**:
- Add custom startup sequence
- Implement background tasks
- Add update checking

### login_enhanced.py
**Purpose**: User authentication UI

**Classes**:
```python
class EnhancedLoginWindow:
    def setup_ui()  # Create login form
    def handle_login()  # Verify credentials
    def handle_guest_login()  # Guest mode
    def show_register_window()  # New user
```

**Features**:
- Responsive login form
- Registration dialog
- Guest mode
- Password validation

**Extension Points**:
- Add two-factor authentication
- Integrate with OAuth/SSO
- Add password recovery
- Implement biometric login

### reservation_panel.py
**Purpose**: Main reservation system UI

**Classes**:
```python
class ReservationSystemWindow:
    def setup_ui()  # Main layout
    def setup_booking_tab()  # New bookings
    def setup_history_tab()  # View history
    def setup_my_bookings_tab()  # User bookings
    def setup_about_tab()  # About page
    
    # Actions
    def book_ticket()
    def search_trains()
    def cancel_booking_dialog()
    def load_my_bookings()
    # ... more methods
```

**Features**:
- Multi-tab interface
- Form validation
- Real-time fare calculation
- Booking history display

**Extension Points**:
- Add more tabs
- Implement advanced search
- Add filtering options
- Create admin dashboard

## Development Workflow

### Adding a New Feature

**Step 1: Plan**
- Define feature scope
- Design data structure
- Update config if needed

**Step 2: Backend**
- Add to database module if data storage needed
- Implement business logic

**Step 3: Frontend**
- Create UI components in ui_utils.py
- Integrate in main window

**Step 4: Test**
- Test with demo data
- Verify edge cases
- Check responsiveness

**Step 5: Document**
- Update USAGE.md
- Add code comments
- Update this guide

### Example: Adding New Train Class

**File**: config.py
```python
# In TrainData class
CLASSES = ["Sleeper", "AC 3-Tier", "AC 2-Tier", "AC 1-Tier", "General", "Luxury"]

# In FareCalculator
BASE_FARES = {
    "Sleeper": 500,
    "AC 3-Tier": 1000,
    "AC 2-Tier": 1500,
    "AC 1-Tier": 2500,
    "General": 250,
    "Luxury": 5000  # New
}
```

**File**: reservation_panel.py
```python
# Update dropdown
self.class_combo = StyledCombobox(
    travel_frame, values=TrainData.CLASSES
)
```

### Example: Adding Notifications

**File**: database.py
```python
def save_booking(booking_data):
    # ... existing code
    # Add email notification
    send_confirmation_email(booking_data['email'], booking_id)
```

## Code Style Guide

### Naming Conventions
```python
# Classes: PascalCase
class BookingDatabase:
    pass

# Functions/Methods: snake_case
def save_booking():
    pass

# Constants: UPPER_CASE
DATABASE_PATH = "/path/to/db"

# Private variables: _leading_underscore
self._private_var = value
```

### Documentation
```python
def calculate_fare(from_station, to_station, travel_class):
    """
    Calculate total fare for a journey.
    
    Args:
        from_station (str): Origin station name
        to_station (str): Destination station name
        travel_class (str): Class of travel
    
    Returns:
        float: Calculated fare in rupees
    
    Example:
        >>> calculate_fare("Delhi", "Mumbai", "AC 2-Tier")
        1770.0
    """
    pass
```

### Comments
```python
# Good: Explains WHY
if len(password) < 6:
    # Passwords must be at least 6 chars per security policy
    return False

# Bad: Explains WHAT (obvious from code)
# Check if password is short
if len(password) < 6:
    return False
```

## Testing

### Manual Testing Checklist

```
[ ] Login with correct credentials
[ ] Login with wrong credentials
[ ] Register new account
[ ] Make booking with all fields
[ ] Make booking with minimal fields
[ ] Generate PDF ticket
[ ] View booking history
[ ] Cancel booking
[ ] Check responsive UI
[ ] Test all buttons
[ ] Verify data persistence
[ ] Check error messages
```

### Unit Testing Template

```python
import unittest
from database import BookingDatabase

class TestBookingDatabase(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.booking_data = {
            'full_name': 'Test User',
            'from_station': 'Delhi',
            'to_station': 'Mumbai'
        }
    
    def test_save_booking(self):
        """Test saving a booking"""
        booking_id = BookingDatabase.save_booking(self.booking_data)
        self.assertIsNotNone(booking_id)
    
    def test_load_booking(self):
        """Test loading a booking"""
        # ... test code

if __name__ == '__main__':
    unittest.main()
```

## Deployment

### Creating Executable (PyInstaller)

```bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed main.py

# Executable in: dist/main.exe
```

### Distribution Package

```bash
# Create setup.py
python setup.py sdist bdist_wheel

# Upload to PyPI
twine upload dist/*
```

## Performance Optimization

### Current Performance
- Startup time: ~2 seconds
- PDF generation: 1-2 seconds
- Memory usage: 50-100MB

### Optimization Strategies

```python
# 1. Lazy loading
if large_data_needed:
    from expensive_module import function
    
# 2. Caching
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_calculation(x):
    return x ** 2

# 3. Threading for long operations
def long_operation():
    threading.Thread(target=slow_function, daemon=True).start()
```

## Security Considerations

### Current (Demo Only)
- Plain text passwords
- Local file storage
- No encryption

### Production Recommendations

```python
# 1. Password hashing
from argon2 import PasswordHasher
ph = PasswordHasher()
hashed = ph.hash("password")

# 2. Secure storage
import keyring
keyring.set_password("A.R.Y.A", username, password)

# 3. API security
import requests
requests.post(url, json=data, verify=True, timeout=5)

# 4. Input validation
import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

## Debugging Tips

### Enable Debug Mode

```python
# In main.py
DEBUG = True

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
    
# In config.py
class AppConfig:
    DEBUG = True
```

### Print Statements

```python
# Good for debugging
print(f"DEBUG: booking_id={booking_id}, status={booking.status}")

# Even better: Use logging
import logging
logger = logging.getLogger(__name__)
logger.debug(f"Processing booking {booking_id}")
```

### Common Errors

```
Error: ModuleNotFoundError: No module named 'qrcode'
→ Fix: pip install qrcode[pil]

Error: TclError: couldn't connect to display
→ Fix: Set DISPLAY environment variable (Linux)

Error: FileNotFoundError: [Errno 2] No such file
→ Fix: Create .aryaRRS directory, check permissions
```

## Git Workflow

```bash
# Clone repository
git clone https://github.com/user/A.R.Y.A.git

# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "feat: Add new feature"

# Push and create pull request
git push origin feature/new-feature
```

## Contributing Guidelines

1. **Code Quality**
   - Follow PEP 8 style guide
   - Use type hints where possible
   - Add docstrings to functions

2. **Testing**
   - Write tests for new code
   - Ensure all tests pass
   - Check coverage

3. **Documentation**
   - Update relevant docs
   - Add comments for complex code
   - Update CHANGELOG

4. **Commit Messages**
   - Use conventional commits
   - Example: `feat: Add passenger search filter`

## Roadmap

### Version 2.0 (Current)
- ✅ Responsive UI
- ✅ QR code tickets
- ✅ User authentication
- ✅ Booking management

### Version 2.1 (Planned)
- [ ] Email notifications
- [ ] SMS alerts
- [ ] Advanced search filters
- [ ] Multi-language support

### Version 3.0 (Planned)
- [ ] Web interface
- [ ] Mobile app
- [ ] Real-time train tracking
- [ ] Payment gateway
- [ ] Analytics dashboard

---

## Additional Resources

- **Tkinter Documentation**: https://docs.python.org/3/library/tkinter.html
- **FPDF2 Docs**: https://py-pdf.github.io/fpdf2/
- **QRCode Library**: https://github.com/lincolnloop/python-qrcode
- **PEP 8 Style Guide**: https://www.python.org/dev/peps/pep-0008/

---

**Happy Coding!** 🚀

*Last Updated: March 28, 2026*
