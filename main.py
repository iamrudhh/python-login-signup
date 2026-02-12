import hashlib
import json
import os

# Terminal color codes
RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[92m"

# Database file configuration
DB_FILE = "users.json"

# Load Database from JSON File
if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as file:
        database = json.load(file)
else:
    database = {}

# Login Function
def login ():
    login_username = input(">> Enter username : ")
    if login_username not in database : 
        print(RED + "User not found" + RESET)
        return
    login_password = input(">> Enter password : ")
    if database[login_username]["password"] == login_password:
        print(GREEN + f"Wlecome,{login_username} 🎉" + RESET)
    else:
        print(RED + "Password is wrong" + RESET)
    

# Showing Database
def show_database ():
    print(database)
    

# Sign up function
def signup ():
    print("\n")
    print("-------------------")
    print("sign up page")
    print("-------------------")
    signup_username = input(">> Enter Username : ")
    if signup_username in database:
        print(RED + "Username already exist" + RESET)
        return
    while True:
        signup_password = input(">> Enter Password : ")

        # Checking password strength
        if signup_password == signup_username:
            print("Password is same as username")
            continue
        elif len(signup_password) <= 12:
            print("Password must contain 12 character")
            continue
        elif not any(char.isupper() for char in signup_password):
            print("Password must contain a uppercase")
            continue
        elif not any(char.islower() for char in signup_password):
            print("password must contain a lowercase")
            continue
        elif not any(char.isdigit() for char in signup_password):
            print("Password must contain a digit")
            continue
        else :  
            while True:
                signup_mobile = input(">> Enter Mobile : ")
                if not signup_mobile.isdigit() or len(signup_mobile) != 10:
                    print("Mobile must contain 10 digit")
                else:
                    hashed_password = hashlib.sha256(
                    signup_password.encode()
                    ).hexdigest()
                    database[signup_username] = {
                    "password": hashed_password,
                    "mobile" : signup_mobile
                    
                    }
                
                    print(GREEN + "Signup successful 🎉" + RESET)
                    break
        break

# main menu function
def main_menu ():
    while True:
        print("-------------------") 
        print("     MAIN MENU")
        print("-------------------") 
        print("[1] Sign up")
        print("[2] Login")
        print("[3] Show Database")
        print("[4] Exit")
        print("-------------------")
        choice = input("Enter your choice : ")
        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            show_database()
        elif choice == "4":
            print("Exiting..!")
            return
        else:
            print(RED + "Invalid choice" + RESET)
        print("\n")
main_menu ()
