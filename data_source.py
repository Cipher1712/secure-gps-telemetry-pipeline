def get_gps_data(simulate=False, port="/dev/pts/2"):
    if simulate:
        import random
        from datetime import datetime

        return {
            "lat": 12.9716 + random.uniform(-0.001, 0.001),
            "lon": 77.5946 + random.uniform(-0.001, 0.001),
            "timestamp": datetime.utcnow()
        }

    # 🔥 READ FROM SERIAL (NMEA)
    try:
        with open(port, "r") as f:
            line = f.readline().strip()
            return line if line else None
    except Exception as e:
        return None