from cli import welcome_user
from games.brain_calc import main as main_calc
from games.brain_even import main as main_even
from games.brain_gcd import main as main_gcd
from games.brain_prime import main as main_prime
from games.brain_progression import main as main_progression


game_func = main_even
def run_game(game_func):
    
    name = welcome_user
    print(game_func.DESCRIPTION)
    for _ in range(3):
        question, right_answer = game_func()
        print(f"Question: {question}")
        your_answer = int(input("Your answer: "))

        if your_answer != right_answer:
            print(f"'{your_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{right_answer}'")
            print(f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
            
    print(f"Congratulations, {name}!")


def main(game_func):
    run_game(game_func)


if __name__ == "__main__":
    main(game_func)
