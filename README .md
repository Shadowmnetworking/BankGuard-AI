# BankGuard AI

**Developer:** Felix (shadownet)  
**Field:** Cybersecurity | AI | Fraud Detection  
**Location:** Thika, Kenya

## Description
BankGuard AI is a fraud detection system that uses machine learning to identify suspicious financial transactions. Built using Flask, Pandas, and Isolation Forest, it's ideal for banks and fintech teams exploring AI-based fraud prevention.

---

## Features
- Detects anomalous transactions using Isolation Forest
- Real-time transaction analysis via Flask API
- Interactive web dashboard for monitoring flagged transactions
- Logging and basic error handling
- Modular and scalable

---

## Project Structure

```
app.py                   # Main Flask app with all routes
dashboard.html           # Admin dashboard UI
sample_transactions.csv  # Simulated transaction data
requirements.txt         # Project dependencies
test_app.py              # Unit tests
```

---

## Tech Stack
- Python
- Flask
- Scikit-learn
- Pandas
- Joblib

---

## How to Run
1. Clone this repo:
```bash
git clone https://github.com/Shadowmnetworking/BankGuard-AI.git
cd BankGuard-AI
```

2. (Optional) Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python app.py
```

Open in browser: [http://localhost:5000](http://localhost:5000)

---

## API Endpoints

### `POST /detect`
Send a transaction to check if it is fraudulent.

**Sample Request:**
```json
{
  "user_id": "abc123",
  "amount": 5200,
  "location": "Nairobi",
  "device_id": "x2debc1",
  "timestamp": "2025-05-16 14:12:21"
}
```

**Sample Response:**
```json
{
  "result": "Fraudulent",
  "details": {
    "user_id": "abc123",
    "amount": 5200,
    "location": "Nairobi",
    "device_id": "x2debc1",
    "timestamp": "2025-05-16 14:12:21"
  }
}
```

---

### `GET /transactions`
Returns all sample transactions with predicted fraud status.

**Sample Response:**
```json
[
  {
    "user_id": "abc123",
    "amount": 5200,
    "location": "Nairobi",
    "device_id": "x2debc1",
    "timestamp": "2025-05-16 14:12:21",
    "result": "Fraudulent"
  },
  ...
]
```

---

## About the Developer
Felix, also known as shadownet, is a cybersecurity student at Mount Kenya University. He’s passionate about ethical hacking, AI systems, and building tools that banks can use to protect their users.

---

**Let's fight fraud with code.**
