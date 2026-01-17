import prompt

def greet():
    print('Welcome to my application!')

def get_name():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

def main():
    greet()
    get_name()

if __name__ == "__main__":
    main()
