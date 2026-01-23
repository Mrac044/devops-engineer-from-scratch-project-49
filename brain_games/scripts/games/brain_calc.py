from random import randint, choice
from ..cli import welcome_user

def calc():  

    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("What is the result of the expression?")

    operations = ("+", "-", "*")

    for _ in range(3):
        num_1 = randint(1, 20)
        num_2 = randint(1, 20)
        operation = choice(operations)

        if operation == "+":
            right_answer = num_1 + num_2
        elif operation == "-":
            right_answer = num_1 - num_2
        else:
            right_answer = num_1 * num_2
        
        question = f"{num_1} {operation} {num_2}"
        print(f"Question: {question}")
        your_answer = int(input("Your answer: "))

        if your_answer != right_answer:
            print(f"\"{your_answer}\" is wrong answer ;(. Correct answer was \"{right_answer}\"")
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
        
    print(f"Congratulations, {name}!")
    

def main():
    calc()

if __name__ == "__main__":
    main()

