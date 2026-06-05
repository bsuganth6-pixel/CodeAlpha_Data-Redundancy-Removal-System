# 🛡️ Data Redundancy Removal System

> A Python-based system that validates incoming data, detects duplicate records, and ensures only clean, unique entries are stored in the database.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Technologies Used](#technologies-used)

---

## 📖 About the Project

In real-world databases, **duplicate and invalid records** are a major problem — they waste storage, slow down queries, and corrupt data integrity.

This project solves that by building a **Data Redundancy Removal System** that acts as a smart gate before storing any record. Every entry is validated and checked for duplicates before it ever touches the database.

Built with **pure Python** — no external libraries needed.

---

## ✨ Features

| Feature | Description |
|---|---|
| ✅ Data Validation | Checks for empty fields and valid email format |
| 🔍 Duplicate Detection | Detects duplicate ID and duplicate Email |
| ❌ False Positive Handling | Rejects invalid/malformed entries immediately |
| 💾 Unique Storage | Only clean, verified records are saved |
| 📂 Auto Database Setup | Creates `database.csv` automatically on first run |

---

## 📁 Project Structure

```
Data_Redundancy_Removal_System/
│
├── main.py          # Core application logic
├── database.csv     # Auto-generated data store
└── README.md        # You are here
```

---

## ⚙️ How It Works

Every record goes through this pipeline before being saved:

```
New Data Entry
      ↓
 Validate Fields  ──── Fail ──→  "Invalid Data (False Positive)"
      ↓
 Check Duplicate  ──── Fail ──→  "Duplicate Data Found"
      ↓
 Store in CSV     ──────────→   "Unique Record Added Successfully"
```

### Functions

**`validate_data(user_id, name, email)`**
- Rejects empty ID or Name
- Rejects email without `@` or `.`

**`is_duplicate(user_id, email)`**
- Scans existing records for matching ID
- Scans for matching Email (case-insensitive)

**`add_record(user_id, name, email)`**
- Orchestrates validation → duplicate check → save

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed → [Download here](https://www.python.org/downloads/)
- No extra libraries needed (uses built-in `csv` and `os`)

### Setup

```bash
# 1. Clone or download the project
git clone https://github.com/yourusername/data-redundancy-removal-system.git

# 2. Navigate into the folder
cd Data_Redundancy_Removal_System

# 3. Run the program
python main.py
```

> `database.csv` is created automatically on first run.

---

## 💻 Usage

When you run the program, you'll see:

```
--- Data Redundancy Removal System ---
1. Add Record
2. Exit
Enter choice:
```

- Press `1` to add a new record
- Press `2` to exit

---

## 🧪 Sample Output

**✅ Adding a unique record:**
```
Enter ID: 101
Enter Name: Suganth
Enter Email: suganth@gmail.com

Unique Record Added Successfully
```

**❌ Adding a duplicate:**
```
Enter ID: 101
Enter Name: Suganth
Enter Email: suganth@gmail.com

Duplicate Data Found
```

**⚠️ Invalid email:**
```
Enter ID: 102
Enter Name: Ravi
Enter Email: ravi-gmail

Invalid Data (False Positive)
```

**📂 database.csv after adding records:**
```
ID,Name,Email
101,Suganth,suganth@gmail.com
```

---

## 🛠️ Technologies Used

- **Python 3** — Core language
- **csv module** — Reading and writing the database
- **os module** — File existence check
- **CSV flat file** — Lightweight persistent storage

---

## 🎓 Course Info

- **Course:** Cloud Computing / Data Management
- **College:** Prathyusha Engineering College
- **Department:** B.E. CSE (Cybersecurity)

---

> Made with 💙 by Mamaa
