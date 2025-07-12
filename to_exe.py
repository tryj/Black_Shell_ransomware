import os

os.system("pip install pyinstaller")
os.system(r'pyinstaller --noconfirm --onefile --console --icon "image\logo.ico"  "encrypt.py"')
os.system(r'pyinstaller --noconfirm --onefile --console --icon "image\logo.ico"  "decrypt.py"')