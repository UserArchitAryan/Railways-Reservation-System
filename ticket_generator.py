# PDF and QR Code Generation Module

import qrcode
from fpdf import FPDF
from io import BytesIO
import os
from config import AppConfig, Colors
from datetime import datetime

class TicketPDFGenerator:
    """Generate professional railway tickets with QR codes"""
    
    @staticmethod
    def generate_ticket_pdf(booking_data):
        """Generate professional ticket PDF"""
        try:
            pdf = FPDF(orientation='P', unit='mm', format='A4')
            pdf.add_page()
            pdf.set_left_margin(10)
            pdf.set_right_margin(10)
            pdf.set_top_margin(10)
            
            # Header
            pdf.set_font("Arial", "B", 18)
            pdf.set_text_color(30, 136, 229)
            pdf.cell(0, 10, "A.R.Y.A - RAILWAY TICKET", ln=True, align='C')
            
            # Booking Reference
            pdf.set_font("Arial", "B", 12)
            pdf.set_text_color(50, 50, 50)
            pdf.cell(0, 8, f"Booking Reference: {booking_data.get('booking_id', 'N/A')}", 
                    ln=True, align='C')
            
            # Divider
            pdf.set_draw_color(200, 200, 200)
            pdf.line(10, pdf.get_y() + 2, 200, pdf.get_y() + 2)
            pdf.ln(5)
            
            # Passenger Details
            pdf.set_font("Arial", "B", 11)
            pdf.set_text_color(30, 136, 229)
            pdf.cell(0, 8, "PASSENGER DETAILS", ln=True)
            
            pdf.set_font("Arial", "", 10)
            pdf.set_text_color(50, 50, 50)
            
            details = [
                ("Full Name", booking_data.get('full_name', 'N/A')),
                ("Age", booking_data.get('age', 'N/A')),
                ("Gender", booking_data.get('gender', 'N/A')),
                ("Contact Number", booking_data.get('mobile', 'N/A')),
                ("Email", booking_data.get('email', 'N/A')),
            ]
            
            for label, value in details:
                pdf.set_font("Arial", "B", 10)
                pdf.cell(60, 7, label + ":")
                pdf.set_font("Arial", "", 10)
                pdf.cell(0, 7, str(value), ln=True)
            
            pdf.ln(3)
            
            # Journey Details
            pdf.set_font("Arial", "B", 11)
            pdf.set_text_color(30, 136, 229)
            pdf.cell(0, 8, "JOURNEY DETAILS", ln=True)
            
            pdf.set_font("Arial", "", 10)
            pdf.set_text_color(50, 50, 50)
            
            journey = [
                ("Origin Station", booking_data.get('from_station', 'N/A')),
                ("Destination Station", booking_data.get('to_station', 'N/A')),
                ("Travel Date", booking_data.get('travel_date', 'N/A')),
                ("Train Name/Number", booking_data.get('train_number', 'N/A')),
                ("Class of Travel", booking_data.get('travel_class', 'N/A')),
            ]
            
            for label, value in journey:
                pdf.set_font("Arial", "B", 10)
                pdf.cell(60, 7, label + ":")
                pdf.set_font("Arial", "", 10)
                pdf.cell(0, 7, str(value), ln=True)
            
            pdf.ln(3)
            
            # Reservation Details
            pdf.set_font("Arial", "B", 11)
            pdf.set_text_color(30, 136, 229)
            pdf.cell(0, 8, "RESERVATION DETAILS", ln=True)
            
            pdf.set_font("Arial", "", 10)
            pdf.set_text_color(50, 50, 50)
            
            reservation = [
                ("Quota", booking_data.get('quota', 'N/A')),
                ("Seat Preference", booking_data.get('seat_pref', 'N/A')),
                ("Meal Preference", booking_data.get('meal_pref', 'N/A')),
                ("Coach Type", booking_data.get('coach_type', 'N/A')),
                ("ID Proof", booking_data.get('id_proof', 'N/A')),
                ("Reservation Type", booking_data.get('reservation_type', 'N/A')),
            ]
            
            for label, value in reservation:
                pdf.set_font("Arial", "B", 10)
                pdf.cell(60, 7, label + ":")
                pdf.set_font("Arial", "", 10)
                pdf.cell(0, 7, str(value), ln=True)
            
            pdf.ln(3)
            
            # Fare Details
            pdf.set_font("Arial", "B", 11)
            pdf.set_text_color(30, 136, 229)
            pdf.cell(0, 8, "FARE DETAILS", ln=True)
            
            pdf.set_font("Arial", "", 10)
            pdf.set_text_color(50, 50, 50)
            
            base_fare = booking_data.get('base_fare', 0)
            gst = base_fare * 0.18
            total_fare = base_fare + gst
            
            fare_details = [
                ("Base Fare", f"Rs. {base_fare:.2f}"),
                ("GST (18%)", f"Rs. {gst:.2f}"),
                ("Total Fare", f"Rs. {total_fare:.2f}"),
            ]
            
            for label, value in fare_details:
                pdf.set_font("Arial", "B", 10)
                pdf.cell(60, 7, label + ":")
                pdf.set_font("Arial", "", 10)
                pdf.cell(0, 7, str(value), ln=True)
            
            pdf.ln(5)
            
            # Add QR Code
            pdf.set_font("Arial", "B", 10)
            pdf.cell(0, 8, "BOOKING VERIFICATION", ln=True, align='C')
            
            qr_path = TicketPDFGenerator._generate_qr_code(booking_data)
            if os.path.exists(qr_path):
                pdf.image(qr_path, x=85, y=pdf.get_y() + 2, w=40)
                pdf.ln(42)
                os.remove(qr_path)
            
            pdf.ln(5)
            
            # Footer
            pdf.set_font("Arial", "", 8)
            pdf.set_text_color(150, 150, 150)
            pdf.ln(3)
            pdf.cell(0, 5, "This is a computerized ticket. No signature required.", 
                    ln=True, align='C')
            pdf.cell(0, 5, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 
                    ln=True, align='C')
            pdf.cell(0, 5, "Keep this ticket safely during travel. It is valid only when printed.", 
                    ln=True, align='C')
            
            # Save PDF
            filename = f"{booking_data.get('booking_id', 'ticket')}.pdf"
            filepath = os.path.join(AppConfig.PDFS_DIR, filename)
            pdf.output(filepath)
            
            return filepath
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return None
    
    @staticmethod
    def _generate_qr_code(booking_data):
        """Generate QR code for booking"""
        try:
            qr_data = f"PNR:{booking_data.get('booking_id', 'N/A')}|From:{booking_data.get('from_station', 'N/A')}|To:{booking_data.get('to_station', 'N/A')}|Date:{booking_data.get('travel_date', 'N/A')}"
            
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save temporarily
            temp_path = os.path.join(AppConfig.PDFS_DIR, "temp_qr.png")
            img.save(temp_path)
            return temp_path
        except Exception as e:
            print(f"Error generating QR code: {e}")
            return None


class FareCalculator:
    """Calculate fares based on journey parameters"""
    
    BASE_FARES = {
        "Sleeper": 500,
        "AC 3-Tier": 1000,
        "AC 2-Tier": 1500,
        "AC 1-Tier": 2500,
        "General": 250
    }
    
    DISTANCE_MULTIPLIER = {
        "Short": 1.0,
        "Medium": 1.5,
        "Long": 2.0
    }
    
    @staticmethod
    def estimate_distance(from_station, to_station):
        """Estimate distance between stations (simplified)"""
        # In production, use actual distance data
        stations_list = [
            "Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata",
            "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Indore"
        ]
        
        if from_station in stations_list and to_station in stations_list:
            distance = abs(stations_list.index(from_station) - stations_list.index(to_station))
            if distance < 3:
                return "Short"
            elif distance < 6:
                return "Medium"
            else:
                return "Long"
        return "Medium"
    
    @staticmethod
    def calculate_fare(from_station, to_station, travel_class):
        """Calculate total fare"""
        base_fare = FareCalculator.BASE_FARES.get(travel_class, 500)
        distance_type = FareCalculator.estimate_distance(from_station, to_station)
        multiplier = FareCalculator.DISTANCE_MULTIPLIER.get(distance_type, 1.0)
        
        fare = base_fare * multiplier
        return fare
