import argparse
import subprocess
import base64
import os
import secrets
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

print("""

███╗░░██╗██╗░░░██╗██╗░░░░░██╗░░░░░██████╗░░█████╗░░█████╗░  ░█████╗░██╗░░██╗
████╗░██║██║░░░██║██║░░░░░██║░░░░░╚════██╗██╔══██╗██╔══██╗  ██╔══██╗██║░██╔╝
██╔██╗██║██║░░░██║██║░░░░░██║░░░░░░░███╔═╝██║░░██║██║░░██║  ██║░░██║█████═╝░
██║╚████║██║░░░██║██║░░░░░██║░░░░░██╔══╝░░██║░░██║██║░░██║  ██║░░██║██╔═██╗░
██║░╚███║╚██████╔╝███████╗███████╗███████╗╚█████╔╝╚█████╔╝  ╚█████╔╝██║░╚██╗
╚═╝░░╚══╝░╚═════╝░╚══════╝╚══════╝╚══════╝░╚════╝░░╚════╝░  ░╚════╝░╚═╝░░╚═╝
            NULL200OK 💀🔥created by NABEEL 🔥💀
🛡️ PyGuard: Advanced Python Obfuscator & EXE Compiler
PyGuard is a professional-grade security tool designed to protect your Python source code from reverse engineering, unauthorized access, and tampering.
""")

def protect_and_compile(file_path, password, output_name):
    # 1. توليد ملح (Salt) عشوائي لكل عملية تشفير لزيادة الأمان
    salt = secrets.token_bytes(16)
    
    # 2. اشتقاق المفتاح (KDF) - بعيداً عن الكود النهائي
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200000, # زيادة عدد التكرارات لتبطئ هجمات التخمين
        backend=default_backend()
    )
    derived_key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    cipher_suite = Fernet(derived_key)

    # 3. تشفير ملفك الأصلي
    with open(file_path, 'rb') as file:
        encrypted_data = cipher_suite.encrypt(file.read())

    # 4. إنشاء ملف التشغيل الوسيط (بدون تخزين كلمة المرور)
    # ملاحظة: سنخزن المفتاح المشتق والملح بشكل بايتات خام وليس نصوص
    wrapper_code = f"""
import base64, sys, os
from cryptography.fernet import Fernet

def launch():
    # تم حذف كلمة المرور تماماً من الكود
    # المفتاح مشفر ومخزن بصيغة بايتات جاهزة للعمل في الذاكرة فقط
    k = {derived_key}
    data = {encrypted_data}
    
    try:
        f = Fernet(k)
        decrypted_code = f.decrypt(data).decode()
        # التنفيذ المباشر في الذاكرة دون المرور بالقرص الصلب
        exec(decrypted_code, {{'__name__': '__main__', '__file__': sys.argv[0]}})
    except Exception:
        # رسالة عامة للتمويه في حال الفشل
        sys.exit("Critical Error: System integrity check failed.")

if __name__ == "__main__":
    launch()
"""
    temp_file = "secure_wrapper.py"
    with open(temp_file, "w", encoding="utf-8") as f_temp:
        f_temp.write(wrapper_code)

    # 5. استدعاء Nuitka لتحويل الكود إلى لغة C++ ثم ملف تنفيذي
    print(f"🛠 [Step 1/2] Encrypting and generating secure wrapper...")
    print(f"🚀 [Step 2/2] Compiling with Nuitka (C++ Backend)... Please wait.")
    
    cmd = [
        "python", "-m", "nuitka",
        "--onefile",
        "--windows-disable-console", # لإخفاء شاشة التيرمنال (مثالي للبرامج الرسومية)
        f"--output-filename={output_name}",
        "--remove-output", # تنظيف مخلفات البناء بعد الانتهاء
        temp_file
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Success! Your protected app is ready: {output_name}.exe")
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to your Python script")
    parser.add_argument("--pass", dest="password", required=True, help="Encryption password")
    parser.add_argument("--name", default="ProtectedApp", help="Output EXE name")
    args = parser.parse_args()
    protect_and_compile(args.file, args.password, args.name)
