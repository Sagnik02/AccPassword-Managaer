from cryptography.fernet import Fernet

#wkey() function generates a new key using the Fernet encryption library and writes it to a binary file named "fernetkey.key"
'''def wkey():
    key = Fernet.generate_key()
    with open("fernetkey.key", "wb") as k_file:
        k_file.write(key)'''

def load_key():
    file = open("fernetkey.key", "rb")
    key_user= file.read()
    file.close()
    return key_user

key_user = load_key()
fer_obj = Fernet(key_user)# Fernet object called fer is created

#function to add the new password for a user account
def add_password():
    acc_name = input('Enter the Account Name: ')
    acc_password= input("Enter the Password: ")

    with open('passwords_user.txt', 'a') as file:
        file.write(acc_name + "--" + fer_obj.encrypt(acc_password.encode()).decode()+ "\n")

#function to view the existing passwords
def view_password():
    try:
        with open('passwords_user.txt', 'r') as file: #The with statement is used here to ensure that the file is properly closed when the block is exited.
            for line in file.readlines():
                data = line.rstrip()
                user, passw = data.split("--")
                print("Account Name :", user, "-- Password :",fer_obj.decrypt(passw.encode()).decode())
    except FileNotFoundError:
        print("That file was not found")

while True:
    user_choice = input("Enter v to view the existing passwords ,enter a to add new password and press e to quit? ").lower()
    if user_choice == "e":
        break
    if user_choice == "v":
        view_password()
    elif user_choice == "a":
        add_password()
    else:
        print("Invalid Entry")
        continue