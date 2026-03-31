from random import randint, choice


DESCRIPTION = "What is the result of the expression?"


def get_question_and_answer():  

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


