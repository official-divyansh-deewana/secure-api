from fastapi import FastAPI
from cryptography.fernet import Fernet

app = FastAPI()

key = b'JwDlqAE4pAwkB1-RVzaMim46I4wNrN1uFpr5Yhv3NmU='
encrypted_content = b'PUT_YOUR_LONG_CODE_HERE'

@app.get("/")
def home():
    return {"status": "API running 🚀"}

@app.get("/decrypt")
def decrypt_data():
    try:
        cipher = Fernet(key)
        decrypted = cipher.decrypt(encrypted_content).decode()
        return {"preview": decrypted[:200]}
    except:
        return {"error": "failed"}
