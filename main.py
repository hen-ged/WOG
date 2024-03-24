from apps.app  import welcome, start_play
from config.utils import Screen_cleaner

welcome()
while True:
    start_play()
    play_more = input('Choose N key to stop or press any key to continue: ')
    if play_more == 'N' or play_more == 'n':
        break
    else:
        Screen_cleaner()
