from random import randint
from ..cli import welcome_user

def prime():

    def is_prime(num):

        divisors = []

        for i in range(1, num // 2 + 1):
            if num % i == 0:
                divisors.append(i)
        
        return "yes" if len(divisors) == 1 else "no"

    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")

    for _ in range(3):
        question = randint(1, 101)
        right_answer = is_prime(question)
        print(f"Question: {question}")
        your_answer = input("Your answer: ")

        if your_answer != right_answer:
            print(f"\"{your_answer}\" is wrong answer ;(. Correct answer was \"{right_answer}\"")
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
        
    print(f"Congratulation, {name}!")

def main():
    prime()

if __name__ == "__main__":
    main()
        

