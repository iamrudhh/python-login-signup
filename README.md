**Simple Python Auth System 🔐**
A lightweight, terminal-based User Authentication System built with Python. This project demonstrates how to handle user registration, login, and secure data storage using JSON and SHA-256 hashing.

**🌟 Features**
User Signup: Validates password strength (length, case, and digits).

Secure Storage: Passwords are never stored in plain text; they are hashed using the hashlib library.

Persistent Database: Saves user data to a users.json file so accounts persist after closing the program.

Data Validation: Ensures mobile numbers are exactly 10 digits and usernames are unique.

Color-Coded Terminal: Uses ANSI escape codes for clear success (green) and error (red) messages.

**🛠️ Requirements**
Python 3.x

No external libraries required (uses built-in json, hashlib, and os).

**🚀 How to Run**
Clone the repository:

Bash
git clone https://github.com/iamrudhh/python-login-signup
cd python-login-signup
Run the script:

Bash
python main.py
📂 Project Structure
main.py: The primary script containing the logic for signup, login, and the main menu.

users.json: Created automatically on the first signup to store user credentials securely.

**🧠 What Beginners Can Learn**
1. Password Hashing
Instead of storing a password like Password123!, the system converts it into a unique string of characters (a hash).

2. JSON Persistence
The script uses the json module to convert Python dictionaries into a file format that stays on your hard drive.

3. Input Sanitization
The code includes logic to prevent common errors, such as:

Checking if a username already exists.

Ensuring the mobile number is numeric.

Enforcing password complexity.

**⚠️ Security Note**
This project is for educational purposes. In a real-world production environment, you should use "salting" with your hashes and professional database systems like PostgreSQL or MongoDB.

**🤝 Contributing**
Found a bug or want to add a feature (like a "Delete Account" option)? Feel free to fork the repo and submit a pull request!
