from .cli import welcome_user


def run_game(game_func, DESCRIPTION):
    
    name = str(welcome_user())
    print(DESCRIPTION)
    
    for _ in range(3):
        question, right_answer = game_func()
        print(f"Question: {question}")
        your_answer = (input("Your answer: "))

        if your_answer != right_answer:
            print(f"'{your_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{right_answer}'")
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
            
    print(f"Congratulations, {name}!")


def main(game_func, DESCRIPTION):
    game_func = game_func()             # func unpacking
    run_game(game_func, DESCRIPTION)


if __name__ == "__main__":
    main(game_func, DESCRIPTION)
