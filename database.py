import os
import validation
import ast

user_db_path = "data/user_record/"
#find user
def does_email_exist(email):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        user_list = ast.literal_eval(read(user))
        if email in user_list.values():
            return True
    return False

def does_account_number_exist(user_account_number):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(user_account_number) + ".txt":
            return True
    return False

#CRUD
#create record
def create(user_account_number, user_details):

    if does_account_number_exist(user_account_number):
        return False
    user_email = user_details["Email"]
    if does_email_exist(user_email):
        print("Email is already in use")
        return False

    completion_state = False
    try:
        f = open(user_db_path + str(user_account_number) + ".txt", "x")
    except FileExistsError:
        print("User already exists")
        #check contents of file before deleting
        #if file is empty then delete
        #delete(account_number)
    else:
        f.write(str(user_details))
    finally:
        f.close()
        completion_state = True
        return completion_state

#read record
def read(user_account_number):
    is_valid_account_number = validation.account_number_validation(user_account_number)

    try:
        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")
    except FileNotFoundError:
        print("User not found")
    except FileExistsError:
        print("User doesn't exist")
    except TypeError:
        print("Invalid account number format")
    else:
        return f.readline()
        
#update record
def update(user_account_number):
    print("update user record")
    #find user with account number
    #fetch contents of the file
    #update the contents of the file
    #save the file
    #return true

#delete record
def delete(user_account_number):
    print(print("delete user record"))
    is_delete_successful = False
    try:
        os.remove(user_db_path + str(user_account_number) + ".txt")
        is_delete_successful = True
    except FileNotFoundError:
        print("User not found") 
    finally:
        return is_delete_successful

def autenticate(user_account_number, password):
    if does_account_number_exist(user_account_number):
        user = ast.literal_eval(read(user_account_number))

        if password == user["Password"]:
            return user
    print("Invalid credentials. Please try again.")
    return False 