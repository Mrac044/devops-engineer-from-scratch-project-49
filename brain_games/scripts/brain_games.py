from .engine import main as main_run
from .cli import welcome_user
from . import (
    main_calc, 
    main_even,
    main_gcd,
    main_prime,
    main_progression
)

def main():
    welcome_user()


if __name__ == "__main__":
    main()

'''
def game_choice():

    game_num = 0

    GAMES = {
        'calc': [main_calc, "What is the result of the expression?"],
        'even': [main_even, "Answer \"yes\" if the number is even, otherwise answer \"no\"."],
        'gcd': [main_gcd, "Find the greatest common divisor of given numbers."],
        'prime': [main_prime, "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."],
        'progression': [main_progression, "What number is missing in the progression?"]
    }
    print("Choose the game:\n")
    
    for k, v in GAMES.items():
        game_num += 1
        print(f"{game_num}. {k}: {v[1]}")

    print()

    choiced_game = input("Your choice (enter the game name): ")
    
    while choiced_game not in GAMES:
        print("This is not a game :(\n")
        choiced_game = input("Please, enter name of the game:")

    main_run(GAMES[choiced_game][0], GAMES[choiced_game][1])


def main():
    game_choice()


if __name__ == "__main__":
    main()
'''
