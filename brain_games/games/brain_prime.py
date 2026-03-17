from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime():

    question = randint(1, 101)
    right_answer = is_prime(question)

    return question, str(right_answer)


def is_prime(num: int) -> str:

    divisors = []

    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)
        
    return "yes" if len(divisors) == 1 else "no"


def main():
    return prime


if __name__ == "__main__":
    main()
        

