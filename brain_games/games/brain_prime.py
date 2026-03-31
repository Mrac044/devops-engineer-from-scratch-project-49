from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():

    question = randint(1, 101)
    right_answer = is_prime(question)

    return question, str(right_answer)


def is_prime(num: int) -> str:

    divisors = []

    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)
        
    return "yes" if len(divisors) == 1 else "no"
        

