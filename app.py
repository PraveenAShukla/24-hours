from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
from model.explainability import explain_credit_risk

app = Flask(__name__)

# Load pre-trained model
model = pickle.load(open('model/model.pkl', 'rb'))

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    # Collect input data
    data = request.form
    features = pd.DataFrame([{
        'Income': float(data['Income']),
        'DebtToIncomeRatio': float(data['DebtToIncomeRatio']),
        'UtilityTimeliness': int(data['UtilityTimeliness']),
        'SocialSentiment': float(data['SocialSentiment']),
        'GeolocationScore': float(data['GeolocationScore']),
    }])
    
    # Predict risk score
    prediction = model.predict_proba(features)[:, 1] * 100
    return render_template('prediction.html', score=round(prediction[0], 2))

# Explainability Route
@app.route('/explain', methods=['POST'])
def explain():
    # Collect input data
    data = request.form
    features = pd.DataFrame([{
        'Income': float(data['Income']),
        'DebtToIncomeRatio': float(data['DebtToIncomeRatio']),
        'UtilityTimeliness': int(data['UtilityTimeliness']),
        'SocialSentiment': float(data['SocialSentiment']),
        'GeolocationScore': float(data['GeolocationScore']),
    }])
    
    # Get SHAP explanations
    explanations = explain_credit_risk(model, features)
    return render_template('explain.html', explanations=explanations)

if __name__ == '__main__':
    app.run(debug=True)
