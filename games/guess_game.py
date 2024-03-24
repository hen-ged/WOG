import random
from apps.utils import one_digit,space_fix


def generate_number(difficulty):
    secret_number = random.randint(0, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    while True:
        user_input = input(f'Guess a Number from 0 to {difficulty}: ')
        user_input = space_fix(user_input)
        if one_digit(user_input) and user_input.isdigit() and (0 <= int(user_input) <= int(difficulty)):
            return int(user_input)
        else:
            print('invalid value please try again')


def compare_results(pc, user):
    if pc == user:
        result = True
    else:
        result = False
    return result


def play(difficulty):
    pc_number = generate_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    result = compare_results(pc_number, user_number)
    if result:
        print('Congratulations you win the game! :)')
    else:
        print(f'sorry you lost the game :( the number was: {pc_number}')
    return result