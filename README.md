# PhishNuke

PhishNuke is a full-stack phishing detection tool that flags suspicious URLs in real-time using a trained machine learning model and basic threat intelligence. This was a fun personal project I created to explore cybersecurity and machine learning in a hands-on way. Feel free to take a look, test it out, or build on it!

## Features

- Classifies URLs as **Phishing** or **Safe**
- Uses a RandomForestClassifier trained on real phishing datasets
- React-based frontend for interactive URL checking
- Backend integrates WHOIS lookup and entropy calculations
- Clean interface styled with Tailwind and shadcn/ui components

## Tech Stack

- Python (Backend, ML)
- Flask (API server)
- scikit-learn, pandas, numpy, whois
- React (Frontend)
- Tailwind CSS + shadcn/ui

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/phishnuke.git
cd phishnuke
```

---

## Backend Setup (Python)

### 2. Create a virtual environment and install dependencies

```bash
cd backend
python3 -m venv venv
source venv/bin/activate     # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Train the model (or use the provided model)

```bash
python phish_model.py  # This script trains and saves 'phish_model.pkl'
```

### 4. Run the Flask API server

```bash
export FLASK_APP=app.py       # On Windows use: set FLASK_APP=app.py
flask run
```

The server will be running at:
```
http://localhost:5000
```

---

## Frontend Setup (React)

### 5. Install dependencies and run React frontend

```bash
cd frontend
npm install
npm run dev   # Or npm start depending on your setup
```

Make sure the backend is running on port 5000 for the API to connect properly.

---

## API Endpoint

**POST** `/predict`

- **Request Body**:

```json
{ "url": "http://example.com" }
```

- **Response**:

```json
{ "prediction": "Phishing" }  // or "Safe"
```

---

## Sample Dataset

Create a file named `phishing_dataset.csv` with the following structure:

```csv
url_length,num_dots,has_https,path_length,has_ip,entropy,domain_age_days,label
54,2,1,12,0,3.45,400,0
78,5,0,25,0,4.78,30,1
92,3,0,8,1,5.21,0,1
61,2,1,19,0,3.98,700,0
```

`label = 1` means phishing, `label = 0` means safe.

---

## Deployment

- **Backend**: Deploy to platforms like Render, Railway, or Heroku
- **Frontend**: Host with GitHub Pages, Vercel, or Netlify
- Make sure to enable CORS in Flask when deploying across different domains

---

## Notes

- This project was built for fun and educational purposes
- Predictions are based on statistical features and should not be used for real security audits
- Contributions, ideas, or feedback are welcome!

---

## Project Structure

```bash
phishnuke/
├── backend/
│   ├── app.py
│   ├── phish_model.py
│   ├── phish_model.pkl
│   ├── phishing_dataset.csv
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   └── PhishNukeApp.jsx
│   └── package.json
└── README.md
```

#MIT License

Copyright (c) 2025 Leema Caravan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in 
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
THE SOFTWARE.
