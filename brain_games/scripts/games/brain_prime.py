from random import randint
from ..engine import run_game


def prime():

    def is_prime(num):

        divisors = []

        for i in range(1, num // 2 + 1):
            if num % i == 0:
                divisors.append(i)
        
        return "yes" if len(divisors) == 1 else "no"

    question = randint(1, 101)
    right_answer = is_prime(question)

    return question, str(right_answer)


def main():
    return prime


def run():
    run_game(prime, "Answer \"yes\" if given number is prime. Otherwise answer \"no\".")


if __name__ == "__main__":
    main()
        

