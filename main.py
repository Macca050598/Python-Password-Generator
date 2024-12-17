#Password generator
#Creat custom password
#Choose variations inside password
#store password in csv file 
import csv

row = ["id", "account", "password"]
def passwordGenerator():
    print("Hello, welcome to the password generator.")
    print("1. Create a new password")
    print("2. See saved passwords...")
    print("3. Delete all passwords...")
    print("4. Exit password generator...")
    choice = input("Please enter an option 1-4: ")

    if choice == "1":
        account = input("Please choose a name for the password...")
        passLength = input("How many characters long would you like the password to be?")
        specialChar = input("Do you want special characters e.g. !>?.%& (yes/no): ".strip().lower())
        passNumbers = input("Do you want it to include numbers? (yes/no): ".strip().lower())
        
        print(account, passLength, passNumbers, specialChar)
        
    if choice == "2":
        return
    if choice == "3":
        return 
    if choice == "4":
        return
    else:
        print("Error: Please pick a number 1-4...")
        
def csvFile():
    return

def generator():
    return

def main():
    passwordGenerator()
if __name__ == "__main__":
    main()