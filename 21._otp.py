from email import message


class Mail():
    _mail_id = "kunalseth012@gmail.com"
    _password = "ssrefngczvjrgbuk"

def random_otp_pass_mixed():
    try:
        import string
        import random
        otp_temp = ""
        otp_temp += string.ascii_letters
        otp_temp += string.digits
        otp_temp += string.punctuation
        final_pass = random.sample(otp_temp,6)           
        final_pass = "".join(final_pass)
        return f"Your OTP is -{final_pass}"
    except Exception:
        return Exception
def random_otp_pass_num():
    try:
        import random
        import math
        #digits="0123456789"
        OTP=""
        for i in range(6):
        # OTP+=digits[math.floor(random.random()*10)] #floor is use for round ing Example 3.15 -> 4 & 4.68 -> 4 & random.random()*10 is returning number between 0 - 9
            OTP += str(random.randrange(0,9))
        return f"Your OTP is -{OTP}"
    except Exception:
        return Exception


def generate_email_otp_check():
    try:
        from smtplib import SMTP
        smtpObj = SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(Mail._mail_id, Mail._password)
        receivers = input("Enter Your Mail ID -")
        message = random_otp_pass_num()
        smtpObj.sendmail(Mail._mail_id, receivers,message)
        print("Check Your mail ------")
        while True:
            a = input("Enter Your OTP >>: ")
            if a == message[-6:]:
                print("Verified")
                break
            else:
                print("Please Check your OTP again")
    except Exception:
        return Exception

generate_email_otp_check()