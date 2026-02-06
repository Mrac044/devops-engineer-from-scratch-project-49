from .cli import welcome_user

def run_game(game_func):
    
    name = str(welcome_user())
    # print(game_func.DESCRIPTION)
    
    for _ in range(3):
        question, right_answer = game_func()
        print(f"Question: {question}")
        your_answer = (input("Your answer: "))

        if your_answer != right_answer:
            print(f"'{your_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{right_answer}'")
            print(f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
            
    print(f"Congratulations, {name}!")


def main(game_func):
    game_func = game_func()     # Распаковка функции
    run_game(game_func)


if __name__ == "__main__":
    main(game_func)
