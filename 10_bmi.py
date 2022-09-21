from cgitb import reset
def bmi(hei,wei):
    try:
        import colorama
        from colorama import Fore,Style
        colorama.init(autoreset=True)
        hei = hei/100
        BMI=str(round(wei/(hei*hei),2))
        print("your Body Mass Index is: {}".format(Fore.GREEN+Style.BRIGHT+ BMI))
        if(BMI>0):
            if(BMI<=16):
                print(Fore.CYAN+"you are severely underweight")
            elif(BMI<=18.5):
                print(Fore.YELLOW+"you are underweight")
            elif(BMI<=25):
                print(Fore.GREEN+Style.BRIGHT+"you are Healthy")
            elif(BMI<=30):
                print(Fore.RED+"you are overweight")
            else: print(Fore.LIGHTBLUE_EX+"you are severely overweight")
        else:(Fore.RED+"enter valid details")
    except Exception as Ex:
        return (Ex)
Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))
bmi(Height,Weight)