#register
# - username and password
# - generate user id


#login
# - (username or email) and password


#bank operations

#initializing system
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
        haveAccount = int(input("Do you have account with us? \n 1. Yes \n 2. No \n"))
        if(haveAccount == 1):
            login()
            break
        elif(haveAccount == 2):
            print(register())
            break
        else:
            print("You selected an invalid option. Please try again.")

#Login, logout, and exit
def accountSearch(username):
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
        loginAccount = input("Enter username, or email \n")
        loginPassword = input("What is your password? \n")

        for accountNumber,userDetails in database.items():
            if(accountNumber == accountSearch(loginAccount)):
                if(userDetails["Password"] == loginPassword):
                    bankOperation(userDetails)
        else:
            print("Invalid credentials. Please try again.")

def logout():
    login()

def exitProgram():
    print("Thank you for your business, have a great day.")
    exit()

# Registering Operations
def register():
    print("*** Registration Form ***")
    email = input("What is your email address? \n").lower()
    firstName = input("What is your first name? \n")
    lastName = input("What is your last name \n")
    username = input("Create a username \n")
    password = input("Create a password \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = {"First Name" : firstName, "Last Name" : lastName, "Email" : email,"Username" : username, "Password": password, "Balance" : 0}
    print("Your account has been created, Your account number is %s" % accountNumber)
    login()

def generateAccountNumber():
    print("account number generator")
    return random.randrange(0000000000, 9999999999)

#Bank Operations
def bankOperation(user):
    print(f"Welcome {user['First Name']} {user['Last Name']}!")

    while True:
        print("Please select one of the following options.")
        selectedOption = int(input("1. Deposit. \n2. Withdrawal. \n3. Complaint \n4. Logout \n5. Exit \n"))

        if(selectedOption == 1):
            depositOperation(user)
            
        elif(selectedOption == 2):
            withdrawalOperation(user)
            
        elif(selectedOption == 3):
            complaint(user)
        elif(selectedOption == 4):
            logout()
            
        elif(selectedOption == 5):
            exitProgram()
            
        else:
            print("Invalid option selected")

def depositOperation(user):
    print(f"You have ${user['Balance']} in your account")
                
    amountDeposited = int(input("How much would you like to deposit? \n"))
    user["Balance"] = user["Balance"] + amountDeposited
    print(f"Your new balance is ${user['Balance']}")
    anythingMoreCheck(user)


def withdrawalOperation(user):
    print(f"You have ${user['Balance']} in Syour account")

    amountWithdrawn = int(input("How much would you like to withdraw? \n"))
    if(amountWithdrawn <= user["Balance"]):
        user["Balance"] = user["Balance"] - amountWithdrawn 
        print(f"Take your cash. Your new balance is ${user['Balance']}")
        anythingMoreCheck(user)
    elif(amountWithdrawn > user["Balance"]):
        print(f"You do not have enough money in your account for this withdrawal, please select a number smaller than {user['Balance']}")
        withdrawalOperation(user)
    else:
        print("Invalid selection, please try again.")
        anythingMoreCheck(user)

def complaint(user):
    input("What issue will you like to report? \n")
    print("Thank you for contacting us")
    anythingMoreCheck(user) 

def anythingMoreCheck(user):
    selectedOption = int(input("Is there anything else you would like to do today? \n 1. Yes\n 2. No \n"))
    if(selectedOption == 1):
        bankOperation(user)
    elif(selectedOption == 2):
        exitProgram()
    else:
        print("Invalid selection, please try again.")
        anythingMoreCheck(user)
    
#banking system

init()
