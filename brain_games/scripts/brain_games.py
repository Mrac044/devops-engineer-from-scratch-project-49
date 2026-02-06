from .engine import main as main_run
from . import (
    main_calc, 
    main_even,
    main_gcd,
    main_prime,
    main_progression
)


def game_choice():
    GAMES = {
        'calc': main_calc,
        'even': main_even,
        'gcd': main_gcd,
        'prime': main_prime,
        'progression': main_progression
    }
    choiced_game = input()
    main_run(GAMES[choiced_game])


def main():
    game_choice()


if __name__ == "__main__":
    main()



