# 🔐 Secure GPS Telemetry Pipeline

## 🚀 Overview
A real-time secure telemetry pipeline that processes GPS data using NMEA protocol, encrypts it using AES, transmits it over serial communication, and decrypts it at the receiver.

## 🧩 Architecture

NMEA Emulator → Parser → AES Encryption → Serial Transmission → Receiver → Decryption


## ⚙️ Features
- Real-time NMEA parsing (GPGGA, GPRMC)
- AES encryption (EAX mode with authentication)
- Virtual serial communication using socat
- Secure receiver with decryption
- Noise filtering for clean data processing

## 🛠️ Tech Stack
- Python
- PyCryptodome (AES)
- socat (virtual serial ports)

## ▶️ How to Run

### 1. Start virtual ports
```bash
socat -d -d pty,raw,echo=0 pty,raw,echo=0
2. Run receiver
python3 receiver.py
3. Start NMEA emulator
# send to pts/1
4. Run pipeline
python3 main.py
🔐 Security
AES encryption with authentication tag
Tamper detection via verification failure
📌 Future Work
FastAPI backend
Live GPS dashboard
Blockchain-based trust logging
