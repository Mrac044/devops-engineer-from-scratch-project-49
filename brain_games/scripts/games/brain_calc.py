from random import randint, choice


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


if __name__ == "__main__":
    main()

