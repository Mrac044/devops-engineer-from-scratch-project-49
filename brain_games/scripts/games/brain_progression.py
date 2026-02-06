from random import randint


def miss_progression():
    
    DESCRIPTION = "What number is missing in the progression?"
    
    def gen_progression():

        progression_lenght = randint(5, 10)
        progression = [randint(-10, 10)]
        step = randint(3, 11)

        for _ in range(progression_lenght):
            progression.append(progression[-1] + step)

        return progression
        
    progression = gen_progression()
    miss_item = randint(0, len(progression) - 1)
    progression[miss_item], right_answer = "..", progression[miss_item]
    
    question = ""
    
    for i in progression:
        question += str(i) + " "

    question = question.strip()

    return question, str(right_answer)

def main():
    return miss_progression


if __name__ == "__main__":
    main()