#in this program we are craeting acronyms of the given sentece (user) // Acronyms - Is a short from
#It's very useful to Using NLP Technology
#errorMessage are using if you want to print coustomize exception message then you can set it
from cgitb import reset
def genAcronyms(errorMessage = None):
    while True:
        #while True is using becuse the function excute until the valid input is not given
        #taking input form the user
        sentence = input("Enter a Sentence -")
        try:
            if sentence.isdigit() or sentence == "":
                print("Please enter a valid sentence ")
            else:
                #now we need to convert sentence to List using split fun
                new_sen_list = sentence.split()
                #now we are creting a blank variable to store the acronyms
                result = ""
                for i in new_sen_list:
                    result+= i[0].upper()
            return result
        except:
            print(errorMessage or "Invalid Input Try Again!!!!!")
#now we excute the program
a = genAcronyms()
print(a)
