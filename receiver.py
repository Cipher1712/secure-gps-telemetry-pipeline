import json
from encryption import decrypt_data

PORT = "/dev/pts/2"


def is_json(data):
    try:
        json.loads(data)
        return True
    except:
        return False


def receive_data():
    with open(PORT, "r") as f:
        while True:
            line = f.readline()

            if not line:
                continue

            raw = line.strip()

            # 🔥 Ignore NMEA noise
            if not is_json(raw):
                continue

            try:
                encrypted_packet = json.loads(raw)

                print("\n📥 Received Packet:")
                print(json.dumps(encrypted_packet, indent=2))

                # 🔓 DECRYPT HERE
                decrypted = decrypt_data(encrypted_packet)

                if decrypted:
                    print("\n🔓 Decrypted Data:")
                    print(json.dumps(decrypted, indent=2))

            except Exception as e:
                print("Error processing packet:", e)


if __name__ == "__main__":
    receive_data()