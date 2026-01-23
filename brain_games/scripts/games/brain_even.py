from random import randint
from ..cli import welcome_user

def is_even():
    
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")  


    for _ in range(3):
        question = randint(1, 100)
        right_answer = isinstance(question, int) and question % 2 == 0

        if right_answer:
            right_answer = "yes"
        else:
            right_answer = "no"
    
        print(f"Question: {question}")
        your_answer = input("Your answer: ")

        if your_answer != right_answer:
            print(f"\"{your_answer}\" is wrong answer ;(. Correct answer was \"{right_answer}\"")
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
        
    print(f"Congratulations, {name}!")
    
def main():
    is_even()

if __name__ == "__main__":
    main()

