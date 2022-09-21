import random
import time
import string
class password():
    def passGene(self):
        try:
            length_of_pass = int(input("Enter the Length of the Password -"))
            characterList = ""
            characterList += string.ascii_letters
            characterList += string.digits
            characterList += string.punctuation
            final_pass = random.sample(characterList,length_of_pass)
            #password_list = []
            # for i in range(length_of_pass):
            #     randomchar = random.choice(characterList)
            #     password_list.append(randomchar)
            return ("The random password is " + "".join(final_pass))
        except Exception as Ex:
            return Ex
   
    

count = 1
while True:
    print(f"The Password Retriving Count is {count}")
    a = password()
    print(a.passGene())
    count +=1
    if count == 6:
        break
    time.sleep(5) 






# print(a)