from Crypto.Cipher import AES
import base64
import json

SECRET_KEY = b'1234567890123456'  # must be same everywhere


# 🔐 ENCRYPT
def encrypt_data(data):
    json_data = json.dumps(data).encode()

    cipher = AES.new(SECRET_KEY, AES.MODE_EAX)

    ciphertext, tag = cipher.encrypt_and_digest(json_data)

    return {
        "ciphertext": base64.b64encode(ciphertext).decode(),
        "nonce": base64.b64encode(cipher.nonce).decode(),
        "tag": base64.b64encode(tag).decode()
    }


# 🔓 DECRYPT (NEW)
def decrypt_data(encrypted_json):
    try:
        ciphertext = base64.b64decode(encrypted_json["ciphertext"])
        nonce = base64.b64decode(encrypted_json["nonce"])
        tag = base64.b64decode(encrypted_json["tag"])

        cipher = AES.new(SECRET_KEY, AES.MODE_EAX, nonce=nonce)

        decrypted = cipher.decrypt_and_verify(ciphertext, tag)

        return json.loads(decrypted.decode())

    except Exception as e:
        print("❌ Decryption failed:", e)
        return None