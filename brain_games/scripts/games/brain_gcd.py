from random import randint
from ..engine import run_game


def choose_gcd():

    def gcd(num_1, num_2) -> int:

        num_1 = int(num_1)
        num_2 = int(num_2)
    
        stages = [max(num_1, num_2), min(num_1, num_2)]

        while stages[-1] != 0:
            current_mod = stages[-2] % stages[-1]
            stages.append(current_mod)
    
        return stages[-2]
    
    num_1 = randint(1, 50)
    num_2 = randint(1, 50)

    right_answer = gcd(num_1, num_2)
    question = f"{num_1} {num_2}"

    return question, str(right_answer)


def main():
    return choose_gcd


def run():
    run_game(choose_gcd, "Find the greatest common divisor of given numbers.")


if __name__ == "__main__":
    main()