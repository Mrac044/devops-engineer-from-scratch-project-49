from random import randint
from ..cli import welcome_user


def miss_progression():
    
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("What number is missing in the progression?")
    
    def gen_progression():

        progression_lenght = randint(5, 10)
        progression = [randint(-10, 10)]
        step = randint(3, 11)

        for _ in range(progression_lenght):
            progression.append(progression[-1] + step)

        return progression

    for _ in range(3):
        
        progression = gen_progression()
        miss_item = randint(0, len(progression) - 1)
        progression[miss_item], right_answer = "..", progression[miss_item]
    
        question = ""
    
        for i in progression:
            question += str(i) + " "

        question = question.strip()

        print(f"Question: {question}")
        your_answer = int(input("Your answer: "))

        if your_answer != right_answer:
            print(f"'{your_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{right_answer}'")
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
        
    print(f"Congratulations, {name}!")


def main():
    miss_progression()


if __name__ == "__main__":
    main()