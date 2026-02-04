from random import randint


def is_even():

    DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."

    question = randint(1, 100)
    right_answer = isinstance(question, int) and question % 2 == 0

    if right_answer:
        right_answer = "yes"
    else:
        right_answer = "no"
    
    return question, right_answer
    

def main():
    return is_even()


if __name__ == "__main__":
    main()

