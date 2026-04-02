## 🛡️ PyGuard: Advanced Python Obfuscator & EXE Compiler
PyGuard is a professional-grade security tool designed to protect your Python source code from reverse engineering, unauthorized access, and tampering. It combines AES-256 encryption with C++ compilation to turn your scripts into highly secure, standalone executable files.

## 🌟 Why use PyGuard?
Most Python "compilers" (like PyInstaller) only bundle your code into an archive that can be easily extracted. PyGuard goes further by:

Encrypting the source code using the Fernet (AES) standard.

Removing plain-text passwords from the final binary.

Compiling the logic into C++ using the Nuitka engine.

Executing the code only in memory (RAM), leaving no trace on the hard drive.

## ✨ Key Features
Military-Grade Encryption: Uses PBKDF2HMAC for key derivation and Fernet for data encryption.

C++ Backend: Leverages Nuitka to convert Python to machine code, making decompilation nearly impossible.

GUI Ready: Includes a "No-Console" mode, perfect for protecting graphical applications.

Enhanced Security: No plain-text passwords stored; uses derived byte-keys directly in the compiled binary.

Anti-Tamper: If the encrypted block is modified, the application will refuse to launch.

## 🛠️ How It Works (Step-by-Step)
**1. Key Derivation & Encryption**
The tool takes your script and a password. It uses a unique Salt and 200,000 iterations of SHA256 to create a 32-byte cryptographic key. Your script is then encrypted into a non-readable "blob" of data.

**2. Secure Wrapper Generation**
Instead of saving your password, PyGuard generates a "Wrapper" script. This wrapper contains the encrypted blob and the derived key bytes.

Security Note: Because the wrapper is later compiled into C++, the key bytes are embedded in machine code, making them significantly harder to find than plain text.

**3. C++ Compilation (Nuitka)**
The wrapper is passed to the Nuitka Compiler. Nuitka translates the Python code into C++ and then uses a C++ compiler (like MinGW or VS) to build a native Windows executable (.exe).

**4. In-Memory Execution**
When a user runs the .exe:

The C++ code initializes.

The encryption key is loaded into RAM.

The source code is decrypted inside the memory.

The script executes directly without ever being saved as a temporary file on the disk.

## 🚀 Installation & Usage
**Requirements**
Python 3.x

C++ Compiler: (MinGW64 or Visual Studio) - Nuitka will prompt to download it automatically if missing.

**Libraries:**

Bash
pip install cryptography nuitka
## Usage
git clone https://github.com/NULL200OK/PyGuard-Obfuscator.git

cd PyGuard-Obfuscator

Bash

python pyguard.py --file your_script.py --pass "YourStrongPassword" --name "MyAppName"

## ⚠️ Disclaimer
This tool is intended for protecting intellectual property. No encryption is 100% unhackable, but PyGuard provides a significantly higher barrier than standard bundling tools.
### NOTE :

 you need to run :
 
 python3 -m venv venv 
 
 source venv/bin/activate 
 
 Mybe you need to install ===> sudo apt install patchelf

