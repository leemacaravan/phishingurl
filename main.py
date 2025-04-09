import pandas as pd
import numpy as np
import re
import requests
import whois
import joblib
from urllib.parse import urlparse
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# ------------------ Feature Engineering ------------------
def extract_features(url):
    features = {}
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path

    # Basic features
    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['has_https'] = int(parsed.scheme == 'https')
    features['path_length'] = len(path)
    features['has_ip'] = int(bool(re.match(r'^(\d{1,3}\.){3}\d{1,3}$', domain)))
    features['entropy'] = -sum([p * np.log2(p) for p in [float(url.count(c))/len(url) for c in set(url)]])

    # WHOIS features
    try:
        w = whois.whois(domain)
        features['domain_age_days'] = (pd.Timestamp.now() - pd.to_datetime(w.creation_date)).days
    except:
        features['domain_age_days'] = 0

    return pd.DataFrame([features])

# ------------------ ML Model Training ------------------
def train_model():
    df = pd.read_csv("https://raw.githubusercontent.com/LeemaCaravan/phishing-dataset/main/phishing_dataset.csv")
    df.fillna(0, inplace=True)
    
    X = df.drop(columns=['label'])
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print(classification_report(y_test, model.predict(X_test)))
    joblib.dump(model, 'phish_model.pkl')

# ------------------ Prediction ------------------
def predict_url(url):
    model = joblib.load('phish_model.pkl')
    features = extract_features(url)
    prediction = model.predict(features)[0]
    return 'Phishing' if prediction == 1 else 'Safe'

if __name__ == "__main__":
    # Train model if needed
    # train_model()

    # Test a URL
    test_url = input("Enter a URL to check: ")
    print("Prediction:", predict_url(test_url))
