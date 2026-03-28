# USAGE Guide - A.R.Y.A Railway Reservation System v2.0.0

## Table of Contents
1. [Getting Started](#getting-started)
2. [Authentication](#authentication)
3. [Making Bookings](#making-bookings)
4. [Managing Bookings](#managing-bookings)
5. [Viewing History](#viewing-history)
6. [Tickets and PDFs](#tickets-and-pdfs)
7. [Cancellations](#cancellations)
8. [UI Features](#ui-features)
9. [Advanced Features](#advanced-features)
10. [Troubleshooting](#troubleshooting)

---

## Getting Started

### First Time Launch

```bash
# Install dependencies (first time only)
pip install -r requirements.txt

# Run the application
python3 main.py
```

### What You'll See
1. **Splash Screen** (2-3 seconds)
   - Shows initialization progress
   - Displays application version and logo

2. **Login Window**
   - Enter credentials
   - Or continue as guest

3. **Main Window**
   - Multi-tab interface
   - Navigation menu
   - Real-time clock

---

## Authentication

### Logging In

**Method 1: Existing User**
1. Enter username in "Username" field
2. Enter password in "Password" field
3. Check "Remember me" (optional)
4. Click "Sign In"

**Method 2: Create New Account**
1. Click "Create Account" button
2. Enter desired username
3. Enter strong password (minimum 6 characters)
4. Confirm password
5. Click "Create Account"
6. Use new credentials to login

**Method 3: Guest Mode**
1. Click "Continue as Guest"
2. Proceed without account
3. Bookings won't be saved
4. Perfect for trying out features

### Demo Credentials (Pre-configured)

| Username | Password | Type |
|----------|----------|------|
| admin | admin123 | Administrator |
| user | password123 | Regular User |
| test | test123 | Test Account |

**Note**: These are demonstration accounts. Passwords are not encrypted for demo purposes.

---

## Making Bookings

### Step-by-Step Booking Process

#### 1. Navigate to "New Booking" Tab
- Click on the "New Booking" tab in the main window
- You'll see a form with three sections

#### 2. Fill Journey Details

**From Station**
- Click dropdown to select origin station
- Options: Delhi, Mumbai, Chennai, Bangalore, Kolkata, etc.
- Select based on your starting point

**To Station**
- Click dropdown to select destination
- Choose any station other than origin
- Example: Delhi → Mumbai

**Travel Date**
- Click date field to open calendar
- Select desired travel date
- Future dates automatically allowed

#### 3. Enter Passenger Details

**Full Name** (Required)
- Enter your complete name
- Example: John Doe

**Age** (Required)
- Enter your age in numbers
- Required for fare and seat allocation

**Gender** (Optional)
- Select: Male, Female, or Other
- Affects seat assignment

**Email** (Optional)
- Enter valid email address
- Used for confirmation (in real system)

**Mobile** (Optional)
- Enter 10-digit phone number
- Contact for support

#### 4. Select Travel Preferences

**Class of Travel** (Required)
- **General**: Budget option, Rs. 250 base fare
- **Sleeper**: Standard, Rs. 500 base fare
- **AC 3-Tier**: Moderate, Rs. 1000 base fare
- **AC 2-Tier**: Recommended, Rs. 1500 base fare
- **AC 1-Tier**: Premium, Rs. 2500 base fare
- Fare automatically displays below

**Quota** (Optional)
- **General**: Standard booking quota
- **Tatkal**: Last-minute bookings
- **Ladies**: Reserved for women
- **Senior Citizen**: For age 60+
- **PWD**: For persons with disability

**Seat Preference** (Optional)
- **Lower**: Ground level berth
- **Middle**: Middle berth
- **Upper**: Upper berth
- **Side Lower/Upper**: Corner seats

**Meal Preference** (Optional)
- **Veg**: Vegetarian meals
- **Non-Veg**: Non-vegetarian meals
- **No Meal**: Self-arrangement

**ID Proof** (Optional)
- Aadhaar Card
- PAN Card
- Passport
- Voter ID
- Driving License

#### 5. Review and Book

**Fare Estimate**
- Automatically calculates based on distance and class
- Shows: Base Fare + GST (18%)
- Example: Rs. 1500 + Rs. 270 GST = Rs. 1770

**Book Ticket Button**
- Review all details
- Click "Book Ticket"
- Confirmation message appears

#### 6. Get Your Booking Confirmation

You'll receive:
- ✓ Booking ID (PNR number)
- ✓ Confirmation message
- ✓ PDF ticket download location

---

## Managing Bookings

### My Bookings Tab

**View All Your Bookings**
1. Click "My Bookings" tab
2. See list of all your reservations
3. Each entry shows:
   - Booking ID
   - Passenger name
   - Route (From → To)
   - Travel date
   - Class
   - Booking status

**Information Displayed**
```
Booking ID: PNR202603XXXXX
Name: John Doe
From: Delhi → To: Mumbai
Date: 2026-04-15
Class: AC 2-Tier
Status: CONFIRMED
Fare: Rs. 1770
```

**Action Buttons Available**
- **Refresh Bookings**: Reload latest bookings from storage
- **Download Ticket**: Open saved PDF folder
- **Cancel Booking**: Cancel reservation

---

## Viewing History

### Booking History Tab

**Purpose**: View historical data of all bookings (system-wide)

**Display Format**
- Table view with columns:
  - Date: Travel date
  - From: Origin station
  - To: Destination
  - Class: Travel class
  - Status: Booking status
  - Fare: Total amount

**Features**
- Shows last 10 bookings
- Can sort by clicking column headers
- Scrollable list
- Updates in real-time

**Update History**
- Click "Reload History" button
- Fetches latest bookings

---

## Tickets and PDFs

### Automatic Ticket Generation

**When Generated**
- Automatically created during booking confirmation
- Saved instantly to local storage

**What's Included**
- Booking reference (PNR)
- Passenger details
- Journey information
- Travel preferences
- Fare breakdown
- **QR Code** (for verification)
- Booking date/time
- Legal disclaimers

### Ticket File Location

**Windows**
```
C:\Users\YourUsername\.aryaRRS\tickets\
```

**Linux**
```
~/.aryaRRS/tickets/
```

**macOS**
```
/Users/YourUsername/.aryaRRS/tickets/
```

### File Naming
```
PNR20260328XXXXX.pdf
```

### Viewing Tickets

**Method 1: Through App**
1. Go to "My Bookings"
2. Click "Download Ticket"
3. Opens folder with all PDFs

**Method 2: Direct Folder Access**
1. Navigate to `.aryaRRS/tickets/` folder
2. Double-click any PDF to view

**Method 3: Windows Explorer**
```
Win + R
%userprofile%\.aryaRRS\tickets\
Enter
```

### PDF Contents

```
═══════════════════════════════════
    A.R.Y.A - RAILWAY TICKET

Booking Reference: PNR202603XXXXX
═══════════════════════════════════

PASSENGER DETAILS
├─ Full Name: John Doe
├─ Age: 28
├─ Gender: Male
├─ Contact: +91-9876543210
└─ Email: john@example.com

JOURNEY DETAILS
├─ Origin: Delhi
├─ Destination: Mumbai
├─ Travel Date: 2026-04-15
├─ Train: Express 12345
└─ Class: AC 2-Tier

RESERVATION DETAILS
├─ Quota: General
├─ Seat: Lower 23
├─ Meal: Veg
├─ Coach: C
└─ ID: Aadhaar

FARE DETAILS
├─ Base Fare: Rs. 1500
├─ GST (18%): Rs. 270
└─ Total: Rs. 1770

[QR CODE]

Generated: 28-Mar-2026 10:30:45
═══════════════════════════════════
```

---

## Cancellations

### How to Cancel a Booking

#### Step 1: Navigate to Cancellation
1. Go to "My Bookings" tab
2. Click "Cancel Booking" button

#### Step 2: Enter Booking ID
1. Dialog box appears
2. Enter your Booking ID (PNR)
3. Example: PNR202603XXXXX

#### Step 3: Confirm Cancellation
1. Double-check booking ID
2. Click "Cancel Booking"
3. Confirmation appears

#### Step 4: Verify Cancellation
1. Go to "My Bookings"
2. Check status: should show "CANCELLED"
3. Note refund details

### Refund Policy (Demo)

**Current Status**
- Full refund: 100% (before travel date)
- Demo system: Instant processing

**Refund Timeline (Real System)**
- T-7 days or more: 100% refund
- T-3 to 7 days: 75% refund
- T-1 to 3 days: 50% refund
- Same day: 25% refund

### Cannot Cancel If
- Already traveled
- Cancellation deadline passed
- Booking already cancelled

---

## UI Features

### Main Window Layout

```
┌─────────────────────────────────────────────────┐
│  A.R.Y.A - RAILWAY RESERVATION SYSTEM          │
├─────────────────────────────────────────────────┤
│ Time: 10:30:45 | Friday | 28/03/2026 │ Logout  │
├─────────────────────────────────────────────────┤
│ ┌─────────┬──────────┬──────────┬────────────┐ │
│ │ New     │ Booking  │ My       │ About      │ │
│ │ Booking │ History  │ Bookings │            │ │
│ └─────────┴──────────┴──────────┴────────────┘ │
│                                                  │
│  [Content Area - Tab Specific]                  │
│                                                  │
│  [Action Buttons]                               │
└─────────────────────────────────────────────────┘
```

### Navigation Elements

**Tabs**
- New Booking: Make new reservations
- Booking History: View system history
- My Bookings: Your reservations
- About: Application information

**Top Bar**
- Real-time clock
- Username display
- Logout button

**Buttons**
- Hover effects (color changes)
- Click feedback
- Responsive sizing

### Responsive Design

**Adapts To Screen Size**
- Automatically scales fonts
- Adjusts layouts
- Maintains proportions
- Works on all resolutions

**Minimum Resolution**: 800x600 pixels
**Recommended**: 1024x768 or higher

---

## Advanced Features

### Search Trains

1. Go to "New Booking" tab
2. Select From and To stations
3. Click "Search Trains"
4. See available trains
5. Select train number

### Fare Calculator

**Automatic Calculation**
- Based on distance between stations
- Varies by travel class
- Includes GST (18%)
- Updates real-time as you select options

**Formula**
```
Total Fare = (Base Fare × Distance Multiplier) × 1.18
```

### User Database

**Local Storage**
- Text-based user file
- Saved in `.aryaRRS/users.json`
- Contains username and password
- For demo only (not encrypted)

**Adding New Users**
1. Click "Create Account" at login
2. Enter username and password
3. Account created instantly
4. Can login immediately

### Booking Database

**File Structure**
```
.aryaRRS/
├── bookings/
│   ├── PNR202603001.json
│   ├── PNR202603002.json
│   └── ...
├── tickets/
│   ├── PNR202603001.pdf
│   ├── PNR202603002.pdf
│   └── ...
├── users.json
└── logs/
```

### Data Persistence

**Automatic Saving**
- Bookings saved instantly
- No manual save needed
- Data survives application restart

**Data Retrieval**
- Multi-user support
- Search by username
- Filter by status
- Sort by date

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: Can't Login

**Problem**: "Invalid username or password" error
- **Solution 1**: Check caps lock is off
- **Solution 2**: Verify spelling of username
- **Solution 3**: Use demo credentials: `user` / `password123`
- **Solution 4**: Create new account with "Create Account" button

#### Issue: Form Won't Submit

**Problem**: Booking button doesn't work
- **Solution**: Fill all **required fields** marked with asterisk
- **Solution**: Check age is entered as numbers only
- **Solution**: Ensure email has @ symbol

#### Issue: PDF Not Found

**Problem**: Can't find downloaded ticket
- **Solution 1**: Check correct folder: `~/.aryaRRS/tickets/`
- **Solution 2**: Use file explorer to navigate
- **Solution 3**: Search for `.pdf` files on computer
- **Solution 4**: Check file permissions

#### Issue: Application Won't Start

**Problem**: "ModuleNotFoundError" when running
- **Solution**: Reinstall dependencies
  ```bash
  pip install --upgrade -r requirements.txt
  ```

#### Issue: Slow Performance

**Problem**: Application lags or freezes
- **Solution 1**: Close other applications
- **Solution 2**: Restart application
- **Solution 3**: Clear old bookings from `.aryaRRS/bookings/`

#### Issue: UI Text Too Small

**Problem**: Can't read text clearly
- **Solution 1**: Increase screen resolution in Windows/Mac settings
- **Solution 2**: Use zoom feature (Chrome: Ctrl+scroll)
- **Solution 3**: Adjust monitor distance

#### Issue: QR Code Not Visible

**Problem**: QR code missing from PDF
- **Solution 1**: Reinstall `qrcode[pil]`: `pip install --upgrade qrcode[pil]`
- **Solution 2**: Check PDF viewer supports images
- **Solution 3**: Regenerate ticket

### Checking Application Status

**Verify Installation**
```bash
python3 -c "import tkinter; print('✓ Tkinter installed')"
python3 -c "import qrcode; print('✓ QR Code installed')"
python3 -c "from fpdf import FPDF; print('✓ FPDF installed')"
```

**View Application Logs**
```bash
cat ~/.aryaRRS/logs/application.log
```

**Check Data Files**
```bash
ls ~/.aryaRRS/bookings/
ls ~/.aryaRRS/tickets/
```

---

## Tips & Best Practices

### Using the System Effectively

1. **Organization**
   - Keep track of your Booking IDs
   - Save important booking emails
   - Keep tickets organized

2. **Booking Management**
   - Make bookings early
   - Check availability first
   - Review all details before confirming

3. **Data Safety**
   - Backup bookings periodically
   - Keep copies of important PDFs
   - Note cancellation deadlines

4. **Efficiency**
   - Use "Remember me" for faster login
   - Complete profile for quicker future bookings
   - Use same email for tracking

---

## Getting Help

**For Issues:**
1. Check this USAGE guide thoroughly
2. Review error message details
3. Check QUICKSTART.md for basic help
4. Review README_v2.md for architecture
5. Check configuration in `config.py`

**For Feature Requests:**
- Review roadmap in README_v2.md
- Check what's planned for v3.0

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Submit login form |
| `Tab` | Move to next field |
| `Shift+Tab` | Move to previous field |
| `Ctrl+Q` | Quit application |
| `Ctrl+L` | Logout |

---

## System Requirements

**Minimum**
- Python 3.8+
- 50 MB disk space
- 800x600 screen resolution
- 512 MB RAM

**Recommended**
- Python 3.10+
- 100 MB disk space
- 1024x768 screen resolution
- 1 GB RAM
- Modern display (1920x1080)

---

## Final Notes

This is a **demonstration system** designed for learning and evaluation purposes. For production deployment, additional security and database features would be required.

**Happy Traveling with A.R.Y.A!** 🚆

---

*Last Updated: March 28, 2026*
*Documentation Version: 2.0.0*
