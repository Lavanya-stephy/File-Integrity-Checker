# 🛡️ File Integrity Checker

A Python-based File Integrity Checker that monitors files for unauthorized changes by generating and comparing **SHA-256 hashes**. The application creates a baseline of file hashes, stores them in a JSON file, and later verifies file integrity by comparing the current hashes with the stored baseline.

## 📌 Features

- ✅ Create a baseline of files in a selected directory
- ✅ Generate SHA-256 hash values for each file
- ✅ Store baseline hashes in a JSON file
- ✅ Load stored hashes from the JSON file
- ✅ Detect modified files
- ✅ Detect deleted files
- ✅ Detect newly added files
- ✅ Interactive Command Line Interface (CLI)

## 🛠 Technologies Used

- Python 3
- hashlib
- json
- os

## 📂 Project Structure

```
File-Integrity-Checker/
│
├── __pycache__/                 # Python cache files
├── baseline.json                # Stores baseline SHA-256 hashes
├── create_baseline.py           # Creates the baseline of file hashes
├── create_json.py               # Saves hash values into a JSON file
├── integrity_check.py           # Verifies file integrity against the baseline
├── Main.py                      # Main application entry point
├── modify.py                    # Generates SHA-256 hashes for files
└── README.md                    # Project documentation
```

## 🚀 Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd File-Integrity-Checker
```

Run the application:

```bash
python Main.py
```

## 💻 Sample Output

```text
Choose one option:

1. Create Baseline
2. Verify Integrity

Enter Folder path:
D:\New folder

Verifying the integrity of your files...

⚠ apple.txt ---- modified
❌ report.txt ---- deleted
➕ New file detected: notes.txt
➕ New file detected: potato.txt
```

## 🔍 How It Works

### 1️⃣ Create Baseline

- Select a folder.
- The application calculates the **SHA-256 hash** of every file.
- The filename and its corresponding hash value are stored in a **JSON** file using `json.dump()`.

### 2️⃣ Verify Integrity

- The application loads the stored baseline using `json.load()`.
- Current SHA-256 hashes are generated for every file.
- The current hashes are compared with the stored baseline to identify:
  - Modified files
  - Deleted files
  - Newly added files

## 🔐 SHA-256 Hashing

SHA-256 is a cryptographic hash algorithm that generates a unique 256-bit hash for every file.

If even a single byte of a file changes, its SHA-256 hash changes completely, making it useful for detecting file tampering.

## 📚 Python Concepts Used

- File Handling
- Dictionary Operations
- JSON Serialization (`json.dump`)
- JSON Deserialization (`json.load`)
- SHA-256 Hashing (`hashlib`)
- Functions
- Loops
- Exception Handling

## ⚠ Disclaimer

This project is developed for educational purposes to demonstrate the principles of file integrity monitoring using cryptographic hashing.

## 📜 License

This project is developed for educational purposes.