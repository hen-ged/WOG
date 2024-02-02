import random
import os
from time import sleep


# func to ignore space
def space_fix(space):
    if ' ' in space:
        space = space.strip()
    return space


def generate_sequence(difficulty):
    random_list = []
    for i in range(0, difficulty):
        random_list_numbers = random.randint(1, 101)
        random_list.append(random_list_numbers)
    print(random_list)
    sleep(0.7)
    os.system('cls')
    return random_list


def get_list_from_user(difficulty):
    input_list = []
    while len(input_list) < difficulty:
        user_list_input = input('input one number at a time to fill the list you remember: ')
        user_list_input = space_fix(user_list_input)
        if user_list_input.isnumeric():
            input_list.append(int(user_list_input))
        else:
            print('invalid value please enter the list again')
            input_list.clear()
    return input_list


def is_list_equal(pc, user):
    if pc == user:
        result = True
    else:
        result = False
    return result


def play(difficulty):
    pc_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    if is_list_equal(pc_list, user_list):
        print('Congratulations you win the game! :)')
    else:
        print(f'sorry you lost the game :( the list was: {pc_list} ')
