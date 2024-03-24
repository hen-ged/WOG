import os


# func to screen cleaner
def Screen_cleaner():
    os.system('cls')


# func to see if one digit only
def one_digit(val):
    if len(val) == 1:
        return True


# func to ignore space
def space_fix(space):
    if ' ' in space:
        space = space.strip()
    return space


def file_exist(file):
    file_true = os.path.exists(file)
    return file_true


def replace_txt(file_path, old_string, new_string):
    file = open(file_path, 'r')
    file_data = file.read()
    file_data = file_data.replace(old_string,new_string)
    file = open(file_path, 'w')
    file.write(file_data)


SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = 0
