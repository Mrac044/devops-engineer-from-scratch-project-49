from cli import welcome_user
from games.brain_calc import main as calc_main
from games.brain_even import main as even_main
from games.brain_gcd import main as gcd_main
from games.brain_progression import main as prog_main
from engine import main as run

def greet():
    print('Welcome to my application!')

def brain_games(name): 
    choice = -1

    while choice != 0:
        choice = int(input("""
Выберите игру:
1 - калькулятор
2 - четность числа
3 - нод
4 - progression

0 - выход
Ваш выбор: 
"""))

        match choice:
            case 1:
                run(calc_main, name)
            case 2:
                run(even_main, name)
            case 3:
                run(gcd_main, name)
            case 4:
                run(prog_main, name)

def main():
    greet()
    name = welcome_user()
    brain_games(name)

if __name__ == "__main__":
    main()



