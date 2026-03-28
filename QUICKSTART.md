# QUICKSTART Guide - A.R.Y.A Railway Reservation System

## ⚡ Quick Installation (2 minutes)

### Windows Users
1. Double-click `install.bat`
2. Wait for installation to complete
3. Run `python main.py`

### Linux/macOS Users
```bash
chmod +x install.sh
./install.sh
python3 main.py
```

### Manual Installation
```bash
pip install -r requirements.txt
python3 main.py
```

---

## 🔑 Demo Login Credentials

Copy and paste one of these to login:

**Admin Account:**
- Username: `admin`
- Password: `admin123`

**Regular User:**
- Username: `user`
- Password: `password123`

**Test Account:**
- Username: `test`
- Password: `test123`

**Or: Click "Continue as Guest"** (no login required)

---

## 📖 Basic Usage (5 minutes)

### Step 1: Login
1. Run `python3 main.py`
2. Enter username and password from above
3. Click "Sign In"

### Step 2: Make a Booking
1. Click "New Booking" tab
2. Select **From Station** (e.g., Delhi)
3. Select **To Station** (e.g., Mumbai)
4. Choose **Travel Date**
5. Enter your **Name**
6. Enter your **Age**
7. Select **Gender**
8. Enter **Email** and **Phone**
9. Select **Class** (AC 2-Tier recommended)
10. Click **"Book Ticket"**

### Step 3: Get Your Ticket
- Your ticket PDF automatically saves
- You'll see your Booking ID (PNR)
- Check "My Bookings" tab to see details

### Step 4: Download Ticket
- Tickets are in: `C:\Users\YourName\.aryaRRS\tickets\` (Windows)
- Or: `~/.aryaRRS/tickets/` (Linux/Mac)
- Each PDF has QR code for verification

---

## 🎯 Key Features at a Glance

| Feature | Where | How |
|---------|-------|-----|
| Make Booking | "New Booking" tab | Fill form → Click "Book Ticket" |
| View Tickets | "My Bookings" tab | See all your bookings |
| History | "Booking History" tab | See all recent bookings |
| Cancel Booking | "My Bookings" → "Cancel Booking" | Enter PNR number |
| Download Ticket | Automatic | Check "~/.aryaRRS/tickets/" |
| Create Account | Login screen → "Create Account" | Enter username & password |
| About System | "About" tab | Application info |

---

## 📋 Form Fields Explained

**Journey Details:**
- **From Station**: Starting point (Delhi, Mumbai, etc.)
- **To Station**: Destination
- **Travel Date**: When you want to travel

**Personal Details:**
- **Full Name**: Your name
- **Age**: Your age
- **Gender**: Male/Female/Other
- **Email**: For confirmation
- **Mobile**: Emergency contact

**Travel Preferences:**
- **Class**: Type of accommodation (AC 2-Tier is most popular)
- **Quota**: Booking quota (General recommended)
- **Seat Preference**: Where you prefer to sit
- **Meal Preference**: Food options
- **ID Proof**: Which ID you'll carry

---

## 💡 Tips & Tricks

1. **Fare Estimation**: Fare shows automatically based on distance and class
2. **Demo Data**: Use realistic station names (Delhi, Mumbai, Chennai, etc.)
3. **Multiple Bookings**: Make multiple bookings under same account
4. **Check Email**: Confirm from your email field
5. **Keep PNR**: Always note your Booking ID (PNR) for customer service

---

## ❌ Troubleshooting

**Problem: "Python not found"**
- Install Python 3.8+ from python.org
- Restart command prompt

**Problem: "tkinter not found"**
- Windows: Reinstall Python, check "tcl/tk" option
- Linux: `sudo apt install python3-tk`
- Mac: Already included

**Problem: PDF not generated**
- Check folder permissions
- Ensure disk space available
- Retry booking

**Problem: Application won't start**
- Run: `pip install --upgrade -r requirements.txt`
- Close all Python processes
- Restart application

---

## 🔐 Important Notes

- **Demo System**: This is for demonstration only
- **Real Data**: Do not use real payment information
- **Data Storage**: All data stored locally on your computer
- **No Real Trains**: Train data is for demo only
- **No Real Booking**: Tickets won't work on real railways

---

## 📞 Need More Help?

1. Check the full README_v2.md file
2. Look at config.py for customization options
3. Review error messages carefully
4. Check application logs in `~/.aryaRRS/logs/`

---

## ⏱️ Next Steps

✅ Installation complete
✅ Credentials ready
✅ Now: Run `python3 main.py`

**Have fun with A.R.Y.A!** 🚆

