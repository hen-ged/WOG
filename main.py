import os
from app import welcome, start_play, game_pick, game_difficulty
import memory_game
import guess_game
import currency_roulette_game

while True:
    welcome()
    start_play()
    user_pick = game_pick()
    user_difficulty = game_difficulty()
    print(f'You choose game level {user_difficulty} difficulty for your game')
    if user_pick == 1:
        memory_game.play(user_difficulty)
    elif user_pick == 2:
        guess_game.play(user_difficulty)
    elif user_pick == 3:
        currency_roulette_game.play(user_difficulty)
    play_more = input('Choose N key to stop or press any key to continue: ')
    if play_more == 'N' or play_more == 'n':
        break
    else:
        os.system('cls')
