def parse_nmea(raw_data, device_id="VEHICLE_001"):
    if raw_data is None:
        return None

    raw_data = raw_data.strip()
    parts = raw_data.split(",")

    try:
        if raw_data.startswith("$GPGGA"):
            lat_raw = parts[2]
            lat_dir = parts[3]
            lon_raw = parts[4]
            lon_dir = parts[5]

        elif raw_data.startswith("$GPRMC"):
            # Skip invalid status
            if parts[2] != "A":
                return None

            lat_raw = parts[3]
            lat_dir = parts[4]
            lon_raw = parts[5]
            lon_dir = parts[6]

        else:
            return None

        if not lat_raw or not lon_raw:
            return None

        # Convert latitude
        lat_deg = float(lat_raw[:2])
        lat_min = float(lat_raw[2:])
        latitude = lat_deg + (lat_min / 60)

        # Convert longitude
        lon_deg = float(lon_raw[:3])
        lon_min = float(lon_raw[3:])
        longitude = lon_deg + (lon_min / 60)

        if lat_dir == "S":
            latitude = -latitude
        if lon_dir == "W":
            longitude = -longitude

        return {
            "device_id": device_id,
            "latitude": round(latitude, 6),
            "longitude": round(longitude, 6)
        }

    except:
        return None