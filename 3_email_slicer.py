from operator import index
def slice_email():
    import re
    try:
        while True:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            email = input("Enter Your Email Address -").strip()
            if re.search(regex,email):
                _username = email[:email.index('@')]
                _doamin = email[email.index('@')+1:]
                print (f'The User Name is {_username} & the doamin name is {_doamin}')
                break
            else:
                print("Please Enter A valid email address!!!!!")
    except Exception as Ex:
        print(Ex)
    finally:
        return("Thank You For Using this Program")
#use the above function
a = slice_email()
print(a)