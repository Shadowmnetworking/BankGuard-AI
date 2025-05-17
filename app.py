
# BankGuard AI - Fraud Detection System
# Developer: Felix (shadownet / Huby)

from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

app = Flask(__name__)

# Load or create a sample dataset
data = pd.read_csv('sample_transactions.csv')  # Columns: user_id, amount, location, device_id, timestamp

# Train a model to detect anomalies
model = IsolationForest(contamination=0.02)
data['score'] = model.fit_predict(data[['amount']])  # Simple model using only the 'amount'

# Save model for reuse
joblib.dump(model, 'fraud_model.pkl')

@app.route('/detect', methods=['POST'])
def detect_fraud():
    tx = request.get_json()
    tx_df = pd.DataFrame([tx])
    model = joblib.load('fraud_model.pkl')
    prediction = model.predict(tx_df[['amount']])
    result = 'Fraudulent' if prediction[0] == -1 else 'Legit'
    return jsonify({"result": result, "details": tx})

@app.route('/')
def home():
    return "BankGuard AI - Fraud Detection System Running"

if __name__ == '__main__':
    app.run(debug=True)
