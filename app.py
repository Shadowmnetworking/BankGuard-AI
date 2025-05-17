from flask import Flask, request, jsonify, render_template_string
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import logging
import os

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

DATA_FILE = 'sample_transactions.csv'
MODEL_FILE = 'fraud_model.pkl'

# Train model if not already saved
def load_or_train_model():
    df = pd.read_csv(DATA_FILE)
    model = IsolationForest(contamination=0.02)
    df['score'] = model.fit_predict(df[['amount']])
    joblib.dump(model, MODEL_FILE)

if not os.path.exists(MODEL_FILE):
    load_or_train_model()

# Detect fraud
@app.route('/detect', methods=['POST'])
def detect_fraud():
    tx = request.get_json()
    if not tx or 'amount' not in tx:
        return jsonify({"error": "Missing 'amount' in request data"}), 400
    try:
        tx_df = pd.DataFrame([tx])
        model = joblib.load(MODEL_FILE)
        prediction = model.predict(tx_df[['amount']])
        result = 'Fraudulent' if prediction[0] == -1 else 'Legit'
        logging.info("Transaction processed: %s | Result: %s", tx, result)
        return jsonify({"result": result, "details": tx})
    except Exception as e:
        logging.error("Error during prediction: %s", str(e))
        return jsonify({"error": str(e)}), 500

# Serve transactions with predictions
@app.route('/transactions', methods=['GET'])
def get_transactions():
    try:
        df = pd.read_csv(DATA_FILE)
        model = joblib.load(MODEL_FILE)
        df['result'] = model.predict(df[['amount']])
        df['result'] = df['result'].apply(lambda x: 'Fraudulent' if x == -1 else 'Legit')
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        logging.error("Error loading transactions: %s", str(e))
        return jsonify({"error": str(e)}), 500

# Serve dashboard UI
@app.route('/')
def dashboard():
    try:
        with open('dashboard.html', 'r') as file:
            html = file.read()
        return render_template_string(html)
    except Exception as e:
        logging.error("Dashboard load failed: %s", str(e))
        return "Dashboard not available.", 500

if __name__ == '__main__':
    app.run(debug=True)
