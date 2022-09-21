from random import random
from time import time


def Rolling_Dice():
    try:
        import random
        import time
        min_val_dice = 1
        max_value_dixe = 6
        count = 0
        while True:
            user = input('Enter "C" for "Continue" or if you want to "end" the game the type "E" --- ').upper()
            if user != 'C' or user != 'E':
                print("Plaese Enter Correct Input 'C' or 'E'")
            if user == 'C':
                print("Dice rolling …")
                time.sleep(2)
                print("Dice Rolled")
                print(random.randint(min_val_dice,max_value_dixe))
                count += 1
            if user == 'E':
                print(f"Thank You For Playing the Game, Total {count} time's dice rolled")
                break
    except Exception as Ex:
        return Ex 

Rolling_Dice()