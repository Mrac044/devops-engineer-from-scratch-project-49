from random import randint
from ..engine import run_game


DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."

def is_even():

    question = randint(1, 100)
    right_answer = isinstance(question, int) and question % 2 == 0

    if right_answer:
        right_answer = "yes"
    else:
        right_answer = "no"
    
    return question, str(right_answer)
    

def main():
    return is_even


def run():
    run_game(is_even, DESCRIPTION)


if __name__ == "__main__":
    main()

