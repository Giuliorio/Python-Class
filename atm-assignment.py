import random

database = {
    0000000000 : {
        "First Name" : "Giulio",
        "Last Name" : "Riondino",
        "Email" : "riondino.giulio@gmail.com",
        "Username" : "GiulioR",
        "Password" : "1234",
        "Balance" : 1000
            }
}

def init():
    print("Welcome to bank Python")

    while True:
        print("Select one of the following options.")
        have_account = int(input("Do you have account with us? \n 1. Yes \n 2. No \n"))
        if(have_account == 1):
            login()
            break
        elif(have_account == 2):
            print(register())
            break
        else:
            print("You selected an invalid option. Please try again.")

#Login, logout, and exit
def account_search(username):
    if("@" in username):
        username = username.lower()
    for account in database.keys():
        if(database[account]["Username"] == username):
            return account
        elif(database[account]["Email"] == username):
            return account

def login():
    print("*** Login ***")

    while True:
        login_account = input("Enter username, or email \n")
        login_password = input("What is your password? \n")

        for account_number,user_details in database.items():
            if(account_number == account_search(login_account)):
                if(user_details["Password"] == login_password):
                    bank_operation(user_details)
        else:
            print("Invalid credentials. Please try again.")

def logout():
    login()

def exit_program():
    print("Thank you for your business, have a great day.")
    exit()

# Registering Operations
def register():
    print("*** Registration Form ***")
    email = input("What is your email address? \n").lower()
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name \n")
    username = input("Create a username \n")
    password = input("Create a password \n")

    account_number = generate_account_number()

    database[account_number] = {"First Name" : first_name, "Last Name" : last_name, "Email" : email,"Username" : username, "Password": password, "Balance" : 0}
    print(f"Your account has been created, Your account number is: {account_number}")
    login()

def generate_account_number():
    return random.randrange(0000000000, 9999999999)

#Bank Operations
def bank_operation(user):
    print(f"Welcome {user['First Name']} {user['Last Name']}!")

    while True:
        print("Please select one of the following options.")
        selected_option = int(input("1. Deposit. \n2. Withdrawal. \n3. Complaint \n4. Logout \n5. Exit \n"))

        if(selected_option == 1):
            deposit_operation(user)
            
        elif(selected_option == 2):
            withdrawal_operation(user)
            
        elif(selected_option == 3):
            complaint(user)
        elif(selected_option == 4):
            logout()
            
        elif(selected_option == 5):
            exit_program()
            
        else:
            print("Invalid option selected")

def deposit_operation(user):
    print(f"You have ${user['Balance']} in your account")
                
    amount_deposited = int(input("How much would you like to deposit? \n"))
    user["Balance"] = user["Balance"] + amount_deposited
    print(f"Your new balance is ${user['Balance']}")
    anything_more_check(user)


def withdrawal_operation(user):
    print(f"You have ${user['Balance']} in Syour account")

    amountWithdrawn = int(input("How much would you like to withdraw? \n"))
    if(amountWithdrawn <= user["Balance"]):
        user["Balance"] = user["Balance"] - amountWithdrawn 
        print(f"Take your cash. Your new balance is ${user['Balance']}")
        anything_more_check(user)
    elif(amountWithdrawn > user["Balance"]):
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
    selected_option = int(input("Is there anything else you would like to do today? \n 1. Yes\n 2. No \n"))
    if(selected_option == 1):
        bank_operation(user)
    elif(selected_option == 2):
        exit_program()
    else:
        print("Invalid selection, please try again.")
        anything_more_check(user)
    
#banking system

init()
