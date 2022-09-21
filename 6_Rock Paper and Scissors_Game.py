from platform import machine
from random import random
def Rock_Papaer_Scissors():
    try:
        import random
        player_score = 0
        machine_score = 0
        while True:
            player_choice = input("Enter Your Choice (Rock/Paper/Scissors) & You Wnat to Close the Game the type 'END' - ").title()
            machine_choice = random.choice(['Rock','Paper','Scissorss'])
            if player_choice == machine_choice:
                print('Tie!')
            elif player_choice == 'Rock':
                if machine_choice == 'Paper':
                    print(f'You Lose! {machine_choice} cover {player_choice}')
                    machine_score +=1
                else:
                    print(f'You Win! {player_choice} smash {machine_choice}')
                    player_score +=1 
            elif player_choice == 'Paper':
                if machine_choice == 'Scissorss':
                    print(f'You Lose! {machine_choice} cut {player_choice}')
                    machine_score += 1
                else:
                    print(f'You Win! {player_choice} cover {machine_choice}')
                    player_score +=1
            elif player_choice == 'Scissorss':
                if machine_choice == 'Rock':
                    print(f'You Lose! {machine_choice} broke {player_choice}')
                    machine_score += 1
                else:
                    print(f'You Win! {player_choice} cut {machine_choice}')
                    player_score +=1
            elif player_choice == 'End':
                print("Final Scores:",end=" -->  ")
                return (f"CPU:{machine_score} and PLAYER:{player_score}")
    except Exception as Ex:
        return Ex
a = Rock_Papaer_Scissors()
print(a)