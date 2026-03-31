from .cli import welcome_user


def launch_game(game_module):
    
    name = str(welcome_user())
    print(game_module.DESCRIPTION)
    
    for _ in range(3):
        question, right_answer = game_module.get_question_and_answer()
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
