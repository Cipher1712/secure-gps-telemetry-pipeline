import time
import json
from data_source import get_gps_data
from processor import parse_nmea   # ✅ updated
from encryption import encrypt_data
from serial_sender import send_to_serial

while True:
    # Read raw NMEA data (from serial or emulator)
    raw_data = get_gps_data(simulate=False)
    print("RAW:", raw_data)

    # Parse NMEA → structured JSON
    structured_data = parse_nmea(raw_data)
    print("STRUCTURED:", structured_data)

    if structured_data is None:
        print("Invalid data:", raw_data)
        time.sleep(1)
        continue

    # Encrypt data
    encrypted = encrypt_data(structured_data)

    print("Encrypted Data:")
    print(json.dumps(encrypted, indent=2))

    # Send to serial port
    send_to_serial(json.dumps(encrypted))

    time.sleep(1)