# 🧠 AI-Augmented Forensics Toolkit for Cybercrime Investigation

This repository contains the official implementation of the **AI-Augmented Forensics Toolkit** described in our research paper, designed to streamline digital forensic investigations using artificial intelligence and machine learning. The toolkit leverages deep learning, NLP, and explainable AI (XAI) to automate the detection, classification, and timeline analysis of cybercrime payloads.

> ⚠️ This toolkit was built for experimental and academic use. It aims to demonstrate the integration of AI into real-world cyber forensic workflows.

---

## 🚀 Features

- 🔍 **Automated Payload Classification** using supervised machine learning
- 📊 **Interactive Dashboards** with live visualizations (via Streamlit)
- 🧭 **Timeline-Based Analysis** of cyberattacks
- 🛡️ **High-Severity Threat Identification**
- 📦 Supports `.csv` logs containing payload details with timestamps, severity, and status
- 🧠 Developed for research-grade scalability and forensic insight

---

## 🧪 Live Dashboards

There are **two interactive Streamlit dashboards** in this repo:

### `cybercrime_dashboard.py`
- Loads `payload_timeline.csv` automatically.
- Displays:
  - Total and unique payloads
  - High severity threats and missed detections
  - Payload type distribution and timeline visualization
  - Breakdown by severity and status
  - Critical threats table

### `Analysis.py`
- Requires manual upload of a `.csv` file.
- Similar analytics with added flexibility for custom data injection.

---

## 📂 File Structure

├── Analysis.py # Upload-based Streamlit dashboard ├── cybercrime_dashboard.py # Preloaded dashboard for instant demo ├── payload_timeline.csv # Sample synthetic dataset used in the paper └── README.md # This file


---

## 📊 Sample Dataset

The dataset `payload_timeline.csv` includes:
- `Timestamp`: Date and time of detection
- `Payload_Type`: e.g., Ransomware, Phishing, Rootkit
- `Severity`: High, Medium, Low
- `Status`: Blocked, Missed
- `Source_IP`: Origin of detected payload

You can substitute this with any similarly structured log file.

---

## 🛠️ Requirements

Install the necessary Python packages:
pip install -r requirements.txt

Or manually:
pip install pandas matplotlib seaborn streamlit

Run the preloaded dashboard:
streamlit run cybercrime_dashboard.py

Run the upload-based dashboard:
streamlit run Analysis.py

🧠 Citation
If you use this toolkit in academic work, please cite:

Aarish Sharma, Rishi Singh, Vicky Jha, Parth Kishore, Shivam Maheshwari, Dr. Mukhtiar Singh
AI-Augmented Forensics Toolkit for Cybercrime Investigation
IEEE [Conference], 2025

This project is licensed under the MIT License — see the LICENSE file for details.

