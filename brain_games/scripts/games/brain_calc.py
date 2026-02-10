from random import randint, choice
from ..engine import run_game


DESCRIPTION = "What is the result of the expression?"

def calc():  

    OPERATIONS = ("+", "-", "*")

    num_1 = randint(1, 20)
    num_2 = randint(1, 20)
    operation = choice(OPERATIONS)

    if operation == "+":
        right_answer = num_1 + num_2
    elif operation == "-":
        right_answer = num_1 - num_2
    else:
        right_answer = num_1 * num_2
        
    question = f"{num_1} {operation} {num_2}"

    return question, str(right_answer)


def main():
    return calc


def run():
    run_game(calc, DESCRIPTION)


if __name__ == "__main__":
    main()



