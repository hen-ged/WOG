from utils import space_fix, one_digit
import memory_game
import guess_game
import currency_roulette_game
from score import add_score


def welcome():
    player_name = input('Enter User Name: ')
    print(f'Hi {player_name} and welcome to the World of Games: The Epic Journey')


def start_play():
    list_of_games = {
        1: '1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.',
        2: '2.Guess Game - guess a number and see if you chose like the computer.',
        3: '3.Currency Roulette - try and guess the value of a random amount of USD in ILS'}
    for game in list_of_games:
        print(list_of_games[game])
    user_pick = game_pick()
    user_difficulty = game_difficulty()
    if user_pick == 1:
        memory_result = memory_game.play(user_difficulty)
        if memory_result:
            add_score(user_difficulty)
    elif user_pick == 2:
        guess_game_result = guess_game.play(user_difficulty)
        if guess_game_result:
            add_score(user_difficulty)
    elif user_pick == 3:
        currency_roulette_game_result = currency_roulette_game.play(user_difficulty)
        if currency_roulette_game_result:
            add_score(user_difficulty)


# func for user input for game pick
def game_pick():
    while True:
        game = input('Please choose a game number from the list above to play: ')
        game = space_fix(game)
        if one_digit(game) and game.isdigit() and (1 <= int(game) <= 3):
            return int(game)
        else:
            print('not valid value for the game please try again')


# func for user input for game difficulty
def game_difficulty():
    while True:
        game_level = input('choose game difficulty level between 1 to 5: ')
        game_level = space_fix(game_level)
        if one_digit(game_level) and game_level.isdigit() and (1 <= int(game_level) <= 5):
            return int(game_level)
        else:
            print('not valid value for difficulty level please try again')
