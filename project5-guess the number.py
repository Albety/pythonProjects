import random
logo = """
     __        __   _                            _          _   _            _   _                 _                  ____                     _                ____                      _ 
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __   / ___|_   _  ___  ___ ___(_)_ __   __ _   / ___| __ _ _ __ ___   ___| |
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__| | |  _| | | |/ _ \/ __/ __| | '_ \ / _` | | |  _ / _` | '_ ` _ \ / _ \ |
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |    | |_| | |_| |  __/\__ \__ \ | | | | (_| | | |_| | (_| | | | | | |  __/_|
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \____|\__,_|\___||___/___/_|_| |_|\__, |  \____|\__,_|_| |_| |_|\___(_)
                                                                                                                                                   |___/                                
"""
def start_again():
    print(logo)
    print("I am thinking of a number between 1 and 100.")
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    remaining_attempts = 0
    number_for_guess = random.randint(1,100)

    if level == "easy":
        remaining_attempts = 10
        print(f"You have {remaining_attempts} attempts remaining to guess the game.")
    else:
        remaining_attempts = 5
        print(f"You have {remaining_attempts} attempts remaining to guess the game.")

    should_continue = True
    while should_continue:
        make_guess = int(input("Make your guess: "))
        if make_guess == number_for_guess:
            print(f"Cool! You guessed! Number was {number_for_guess}")
            should_continue = False
        elif make_guess > number_for_guess:
            print("Too High!")
            remaining_attempts -= 1
            print(f"You have {remaining_attempts} attempts remaining to guess the game.")
        else:
            print("Too Low!")
            remaining_attempts -= 1
            print(f"You have {remaining_attempts} attempts remaining to guess the game.")

        if remaining_attempts == 0:
            print("You lose!")
            print(f"This number was {number_for_guess}")
            should_continue = False
            if input("Do you want start again, y or n?") == 'y':
                start_again()

start_again()

