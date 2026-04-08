import time
import random

def decimal_to_nmea(lat, lon):
    lat_deg = int(abs(lat))
    lat_min = (abs(lat) - lat_deg) * 60

    lon_deg = int(abs(lon))
    lon_min = (abs(lon) - lon_deg) * 60

    lat_dir = "N" if lat >= 0 else "S"
    lon_dir = "E" if lon >= 0 else "W"

    lat_str = f"{lat_deg:02d}{lat_min:07.4f}"
    lon_str = f"{lon_deg:03d}{lon_min:07.4f}"

    return lat_str, lat_dir, lon_str, lon_dir


def generate_nmea():
    lat = 12.9716 + random.uniform(-0.0005, 0.0005)
    lon = 77.5946 + random.uniform(-0.0005, 0.0005)

    lat_str, lat_dir, lon_str, lon_dir = decimal_to_nmea(lat, lon)

    gga = f"$GPGGA,123519,{lat_str},{lat_dir},{lon_str},{lon_dir},1,08,0.9,545.4,M,46.9,M,,*47"

    rmc = f"$GPRMC,123519,A,{lat_str},{lat_dir},{lon_str},{lon_dir},022.4,084.4,230394,003.1,W*6A"

    return gga, rmc


PORT = "/dev/pts/1"

with open(PORT, "w") as f:
    while True:
        gga, rmc = generate_nmea()

        print("📡", gga)
        print("📡", rmc)

        f.write(gga + "\n")
        f.write(rmc + "\n")
        f.flush()

        time.sleep(1)