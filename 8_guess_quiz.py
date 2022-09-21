#creating the quiz 
def quiz(guess,ans):
    try:
        import colorama
        from colorama import Fore,Back,Style
        colorama.init(autoreset=True)
        global score
        still_guess = True
        attempt = 1
        max_attempt = 4
        while still_guess and attempt < max_attempt:
            if guess.upper() == ans.upper():
                score+=1
                still_guess = False
                print('Correct Ans ! {}'.format(Fore.GREEN+Style.BRIGHT+ans))
            else:
                if attempt < max_attempt:
                    print(f"The Maximum number of aateempt is {max_attempt} but You have {max_attempt - attempt} No of attempt left",end="------>")
                    guess = input("Plaese Give the Correct Ans - ")
                attempt += 1
        if attempt == max_attempt:
            print(f"You Reached the Maximum number of attempt  \n The Correct ans is {ans}")
    except Exception as Ex:
        return Ex

score = 0

print("Guess the Animal")
guess1 = input("Which bear lives at the North Pole? ")
quiz(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? ")
quiz(guess2, "Cheetah")
guess3 = input("Which is the larget animal? ")
quiz(guess3, "Blue Whale")
print("Your Score is "+ str(score))