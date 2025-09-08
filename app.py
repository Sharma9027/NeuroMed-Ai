from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from datetime import datetime

app = Flask(__name__)
CORS(app)

# --- MySQL Connection ---
DB_NAME = "doctor_dashboard"

# Step 1: Connect without selecting database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shiv@m9027"
)
cursor = db.cursor()

# Step 2: Create database if not exists
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
db.commit()

# Step 3: Reconnect with database selected
db.close()
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shiv@m9027",
    database=DB_NAME
)
cursor = db.cursor(dictionary=True)

# ---------- PATIENTS ----------
@app.route("/patients", methods=["GET"])
def get_patients():
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    return jsonify(patients)

@app.route("/patients", methods=["POST"])
def add_patient():
    data = request.json
    cursor.execute(
        "INSERT INTO patients (first_name, last_name, age, blood_type, email) VALUES (%s,%s,%s,%s,%s)",
        (data["first_name"], data["last_name"], data["age"], data["blood_type"], data["email"])
    )
    db.commit()
    return jsonify({"message": "Patient added successfully."})

# ---------- APPOINTMENTS ----------
@app.route("/appointments", methods=["GET"])
def get_appointments():
    cursor.execute("""
        SELECT a.id, a.appointment_time, a.reason, a.status,
               p.first_name, p.last_name
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
    """)
    appointments = cursor.fetchall()
    return jsonify(appointments)

@app.route("/appointments", methods=["POST"])
def add_appointment():
    data = request.json
    cursor.execute(
        "INSERT INTO appointments (patient_id, appointment_time, reason, status) VALUES (%s,%s,%s,%s)",
        (data["patient_id"], data["appointment_time"], data["reason"], data.get("status", "Pending"))
    )
    db.commit()
    return jsonify({"message": "Appointment added successfully."})

# ---------- PRESCRIPTIONS ----------
@app.route("/prescriptions", methods=["GET"])
def get_prescriptions():
    cursor.execute("""
        SELECT r.id, r.medication, r.dosage, r.frequency, r.duration,
               p.first_name, p.last_name
        FROM prescriptions r
        JOIN patients p ON r.patient_id = p.id
    """)
    prescriptions = cursor.fetchall()
    return jsonify(prescriptions)

@app.route("/prescriptions", methods=["POST"])
def add_prescription():
    data = request.json
    cursor.execute(
        "INSERT INTO prescriptions (patient_id, medication, dosage, frequency, duration) VALUES (%s,%s,%s,%s,%s)",
        (data["patient_id"], data["medication"], data["dosage"], data["frequency"], data["duration"])
    )
    db.commit()
    return jsonify({"message": "Prescription added successfully."})

# ---------- REPORTS ----------
@app.route("/reports", methods=["GET"])
def get_reports():
    cursor.execute("""
        SELECT r.id, r.report_name, r.report_file,
               p.first_name, p.last_name
        FROM reports r
        JOIN patients p ON r.patient_id = p.id
    """)
    reports = cursor.fetchall()
    return jsonify(reports)

@app.route("/reports", methods=["POST"])
def add_report():
    data = request.json
    cursor.execute(
        "INSERT INTO reports (patient_id, report_name, report_file) VALUES (%s,%s,%s)",
        (data["patient_id"], data["report_name"], data["report_file"])
    )
    db.commit()
    return jsonify({"message": "Report uploaded successfully."})

# ---------- RUN SERVER ----------
if __name__ == "__main__":
    app.run(debug=True)
