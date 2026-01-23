from random import randint

def miss_progression():
    
    progression = [randint(-10, 10)]
    step = randint(3, 11)

    for _ in range(9):
        progression.append(progression[-1] + step)

    miss_item = randint(0, len(progression) - 1)
    progression[miss_item], right_answer = "..", progression[miss_item]
    
    question = ""
    
    for i in progression:
        question += str(i) + " "

    question = question.strip()

    return question, str(right_answer)
        
def main():
    return miss_progression()

if __name__ == "__main__":
    main()