# PhishingURL

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
