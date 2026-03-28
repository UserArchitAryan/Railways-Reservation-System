#!/usr/bin/env python3
"""
A.R.Y.A - Automated Railway Reservation System
Main Entry Point v2.0.0

This is the main launcher for the Railway Reservation System.
The application features responsive UI, QR code tickets, and production-ready architecture.
"""

import sys
import os

# Add project directory to path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

def main():
    """Main application entry point"""
    try:
        from launcher import ApplicationLauncher
        
        print("=" * 60)
        print("A.R.Y.A - Automated Railway Reservation System v2.0.0")
        print("=" * 60)
        print("Initializing application...\n")
        
        launcher = ApplicationLauncher()
        launcher.run()
        
    except ImportError as e:
        print(f"\n❌ Import Error: {e}")
        print("\nRequired packages are missing!")
        print("Please install required packages:")
        print("  pip install tk")
        print("  pip install tkcalendar")
        print("  pip install qrcode[pil]")
        print("  pip install fpdf2")
        print("  pip install pillow")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
