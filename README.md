# NeuroMed-Ai 🏥🤖

**NeuroMed-Ai** is an AI-powered healthcare management system with interactive dashboards for doctors and patients. It streamlines appointments, prescriptions, reports, secure messaging, analytics, and wellness tracking — all backed by a Flask + MySQL backend.

---

## ✨ Features

### 👨‍⚕️ Doctor Dashboard
- Manage patients, appointments, prescriptions, and reports  
- AI Assistant for quick commands (*e.g., “Show appointments”*)  
- Global search, dark/light mode toggle, data export  
- Analytics with charts and revenue insights  
- Profile, notification, and security settings  

### 🧑‍🦰 Patient Dashboard
- View and edit personal profile  
- Book and join telehealth appointments  
- Access health records, lab results, and prescriptions  
- Secure messaging with doctors + file sharing  
- Billing & insurance details  
- Wellness tracker (steps, sleep, hydration, health tips)  
- Emergency quick actions (ambulance call, share records)  

### ⚙️ Backend (Flask + MySQL)
- RESTful APIs for:
  - Patients
  - Appointments
  - Prescriptions
  - Reports  
- Automatic DB creation if not present  
- JSON-based responses for frontend integration  

---

## 🛠 Tech Stack
- **Backend**: Python (Flask, MySQL, CORS)
- 
- **Frontend**: HTML, CSS, Tailwind, JavaScript  
- **Database**: MySQL  
- **AI Integration**: In-dashboard assistant  

---

📂 Project Structure
NeuroMed-Ai/
│── app.py              # Flask backend
│── dashboard.html      # Doctor's dashboard
│── Patient.html        # Patient dashboard
│── settings.html       # Wake word settings
│── login.html          # Login page
---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+  
- MySQL Server  

### Installation
```bash
# Clone the repo
git clone https://github.com/your-username/NeuroMed-Ai.git
cd NeuroMed-Ai

# Install dependencies
pip install flask flask-cors mysql-connector-python
