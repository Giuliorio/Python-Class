def account_number_validation(account_number, error=False):
    need_error_msg = error
    
    if account_number:
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True
            except ValueError:
                    if need_error_msg:
                        print("Account numbers should be an integer")
                    return False
        else:
            if need_error_msg:
                print("Account Number needs to be 10 digits")
            return False
    else:
        if need_error_msg:
            print("Account Number is a required field")
        return False

def is_number(input):
    if input:
        try:
            float(input)
            return True
        except ValueError:
            print("Input should be a number")
            return False
    else:
        print("This is a required field. If you want to go back enter $0")
        return False