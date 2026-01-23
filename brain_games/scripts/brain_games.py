from .cli import welcome_user


def greet():
    print('Welcome to my application!')

def main():
    greet()
    welcome_user()

if __name__ == "__main__":
    main()



