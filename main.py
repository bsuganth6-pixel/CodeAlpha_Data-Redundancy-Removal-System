import csv
import os

DATABASE = "database.csv"

if not os.path.exists(DATABASE):
    with open(DATABASE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Email"])

def validate_data(user_id, name, email):
    if not user_id.strip():
        return False
    if not name.strip():
        return False
    if "@" not in email or "." not in email:
        return False
    return True

def is_duplicate(user_id, email):
    with open(DATABASE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["ID"] == user_id or row["Email"].lower() == email.lower():
                return True
    return False

def add_record(user_id, name, email):
    if not validate_data(user_id, name, email):
        print("Invalid Data (False Positive)")
        return
    if is_duplicate(user_id, email):
        print("Duplicate Data Found")
        return
    with open(DATABASE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_id, name, email])
    print("Unique Record Added Successfully")

while True:
    print("\n--- Data Redundancy Removal System ---")
    print("1. Add Record")
    print("2. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_record(input("Enter ID: "), input("Enter Name: "), input("Enter Email: "))
    elif choice == "2":
        break
