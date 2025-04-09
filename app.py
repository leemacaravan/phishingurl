from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np
import re
import whois
from urllib.parse import urlparse

app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load('phish_model.pkl')

# Feature extraction function
def extract_features(url):
    features = {}
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path

    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['has_https'] = int(parsed.scheme == 'https')
    features['path_length'] = len(path)
    features['has_ip'] = int(bool(re.match(r'^(\d{1,3}\.){3}\d{1,3}$', domain)))
    features['entropy'] = -sum(
        [p * np.log2(p) for p in [float(url.count(c)) / len(url) for c in set(url)] if p > 0]
    )

    try:
        w = whois.whois(domain)
        creation_date = pd.to_datetime(w.creation_date)
        if isinstance(creation_date, pd.Series):  # sometimes returns list
            creation_date = creation_date[0]
        features['domain_age_days'] = (pd.Timestamp.now() - creation_date).days
    except:
        features['domain_age_days'] = 0

    return pd.DataFrame([features])

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get('url', '')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        features = extract_features(url)
        prediction = model.predict(features)[0]
        result = 'Phishing' if prediction == 1 else 'Safe'
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
