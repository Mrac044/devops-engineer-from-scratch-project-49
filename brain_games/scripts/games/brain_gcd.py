from random import randint
from ..cli import welcome_user

def choose_gcd():

    def gcd(num_1, num_2) -> int:

        num_1 = int(num_1)
        num_2 = int(num_2)
    
        stages = [max(num_1, num_2), min(num_1, num_2)]

        while stages[-1] != 0:
            current_mod = stages[-2] % stages[-1]
            stages.append(current_mod)
    
        return stages[-2]

    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    
    for _ in range(3):
        num_1 = randint(1, 50)
        num_2 = randint(1, 50)

        right_answer = gcd(num_1, num_2)
        question = f"{num_1} {num_2}"
    
        print(f"Question: {question}")
        your_answer = int(input("Your answer: "))

        if your_answer != right_answer:
            print(f"\"{your_answer}\" is wrong answer ;(. Correct answer was \"{right_answer}\"")
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
        
    print(f"Congratulation, {name}!")

def main():
    return choose_gcd()

if __name__ == "__main__":
    main()