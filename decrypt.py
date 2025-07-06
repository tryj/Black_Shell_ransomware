from cryptography.fernet import Fernet
import os

# โหลดคีย์
key_file = "key.key"
if not os.path.exists(key_file):
    print("❌ Key file not found! Cannot decrypt files.")
    exit()

with open(key_file, "rb") as f:
    key = f.read()

# สร้าง Fernet object
fernet = Fernet(key)

# กำหนดนามสกุลไฟล์ที่ต้องการถอดรหัส
file_extensions = (".exe", ".dll", ".sys", ".bat", ".cmd", ".msi", ".lnk",
".txt", ".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".csv",
".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".ico",
".mp3", ".wav", ".wma", ".ogg", ".mp4", ".avi", ".mov", ".wmv",
".zip", ".rar", ".7z", ".tar", ".gz",
".db", ".mdb", ".accdb", ".sqlite", ".sql",
".html", ".htm", ".css", ".js", ".php", ".c", ".cpp", ".java", ".cs", ".xml", ".json",
".iso", ".log", ".reg", ".torrent")

# วนลูปถอดรหัสไฟล์ในทุกโฟลเดอร์
for root, _, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(file_extensions) and file != "key.key":
            file_path = os.path.join(root, file)
            
            with open(file_path, "rb") as f:
                encrypted_data = f.read()
            
            try:
                decrypted = fernet.decrypt(encrypted_data)

                # เขียนทับไฟล์เดิมด้วยข้อมูลที่ถอดรหัส
                with open(file_path, "wb") as f:
                    f.write(decrypted)
                print(f"Decrypted: {file_path}")
            except:
                print(f"Skipping non-encrypted file: {file_path}")
