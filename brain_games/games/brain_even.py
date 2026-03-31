from random import randint


DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_question_and_answer():

    question = randint(1, 100)
    right_answer = is_num_even(question)

    if right_answer:
        right_answer = "yes"
    else:
        right_answer = "no"
    
    return question, str(right_answer)


def is_num_even(num: int) -> bool:

    answer = isinstance(num, int) and num % 2 == 0

    return answer
