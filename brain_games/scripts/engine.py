from cli import welcome_user

def run_game(game_module, name):

    for _ in range(3):
        question, right_answer = game_module()

        print(f"Question: {question}")
        your_answer = input("Your answer: ")

        if your_answer != right_answer:
            print(f"\"{your_answer}\" is wrong answer ;(. Correct answer was \"{right_answer}\"")
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
        
    print(f"Congratulation, {name}!")

def main(game_module, name):
    run_game(game_module, name)

if __name__ == "__main__":
    main()

    