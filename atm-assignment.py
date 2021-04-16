import random
from getpass import getpass
import validation
import database

def init():
    print("Welcome to bank Python")

    while True:
        print("Select one of the following options.")
        have_account = input("Do you have account with us? \n 1. Yes \n 2. No \n")
        if validation.is_number(have_account):
            have_account = int(have_account)

            if(have_account == 1):
                login()
            elif(have_account == 2):
                register()
            else:
                print("You selected an invalid option. Please try again.")

#Login, logout, and exit
def login():
    print("*** Login ***")

    while True:
        entered_account = input("Enter your account number \n")

        is_valid_account_number = validation.account_number_validation(entered_account, True)

        if is_valid_account_number:
            entered_password = getpass("What is your password? \n")
            user = database.autenticate(entered_account, entered_password)
            if user:
                database.auth_create(user)
                bank_operation(user)

def logout(user):
    database.auth_delete(user)
    init()

def exit_program(user):
    print("Thank you for your business, have a great day.")
    database.auth_delete(user)
    exit()

# Registering Operations
def register():
    print("*** Registration Form ***")
    email = input("What is your email address? \n").lower()
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name \n")
    username = input("Create a username \n")
    password = getpass("Create a password \n")

    account_number = generate_account_number()

    is_user_created = database.create(account_number, {"Account Number" : account_number, "First Name" : first_name, "Last Name" : last_name, "Email" : email,"Username" : username, "Password": password, "Balance" : 0.0})

    if is_user_created:
        print(f"Your account has been created, Your account number is: {account_number}")
        login()
    else:
        print("Something went wrong. Please try again")
        register()
        
def generate_account_number():
    return random.randrange(0000000000, 9999999999)

#Bank Operations
def bank_operation(user):
    print(f"Welcome {user['First Name']} {user['Last Name']}!")

    while True:
        print("Please select one of the following options.")
        selected_option = input("1. Deposit. \n2. Withdrawal. \n3. Complaint \n4. Logout \n5. Exit \n")
        if validation.is_number(selected_option):
            selected_option = int(selected_option)

        if(selected_option == 1):
            deposit_operation(user)
            
        elif(selected_option == 2):
            withdrawal_operation(user)
            
        elif(selected_option == 3):
            complaint(user)
        elif(selected_option == 4):
            logout(user)
            
        elif(selected_option == 5):
            exit_program(user)
            
        else:
            print("Invalid option selected")

def deposit_operation(user):
    print(f"You have ${user['Balance']} in your account")
    while True:
        amount_deposited = input("How much would you like to deposit? \n")
        if validation.is_number(amount_deposited):
            amount_deposited = float(amount_deposited)
            break
                
    user["Balance"] = user["Balance"] + amount_deposited
    database.update(user)
    print(f"Your new balance is ${user['Balance']}")
    anything_more_check(user)


def withdrawal_operation(user):
    print(f"You have ${user['Balance']} in your account")

    while True:
        amount_withdrawn = input("How much would you like to withdraw? \n")
        if validation.is_number(amount_withdrawn):
            amount_withdrawn = float(amount_withdrawn)
            break

    if(amount_withdrawn <= user["Balance"]):
        user["Balance"] = user["Balance"] - amount_withdrawn
        database.update(user)
        print(f"Take your cash. Your new balance is ${user['Balance']}")
        anything_more_check(user)
    elif(amount_withdrawn > user["Balance"]):
        print(f"You do not have enough money in your account for this withdrawal, please select a number smaller than {user['Balance']}")
        withdrawal_operation(user)
    else:
        print("Invalid selection, please try again.")
        anything_more_check(user)

def complaint(user):
    input("What issue will you like to report? \n")
    print("Thank you for contacting us")
    anything_more_check(user) 

def anything_more_check(user):
    while True:
        selected_option = input("Is there anything else you would like to do today? \n 1. Yes\n 2. No \n")
        if validation.is_number(selected_option):
            selected_option = int(selected_option)

            if(selected_option == 1):
                bank_operation(user)
            elif(selected_option == 2):
                exit_program(user)
            else:
                print("Invalid selection, please try again.")
    
#banking system

init()