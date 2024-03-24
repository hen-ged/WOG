import random
import requests
from config.utils import space_fix


def get_money_interval(amount):
    base_url = 'https://api.exchangerate-api.com/v4/latest/'
    from_currency = 'USD'
    to_currency = 'ILS'
    # Fetch latest exchange rates
    response = requests.get(base_url + from_currency)
    data = response.json()

    if 'rates' in data:
        rates = data['rates']

        if from_currency in rates and to_currency in rates:
            conversion_rate = rates[to_currency] / rates[from_currency]
            converted_amount = amount * conversion_rate
            return converted_amount


def get_guess_from_user(secret_number):
    while True:
        user_input = input(f'Guess how much is {secret_number} USD in ILS: ')
        user_input = space_fix(user_input)
        if user_input.isnumeric() or type(user_input) is float:
            return int(user_input)
        else:
            print('invalid value please try again')


def compare_results(converted_currency, user, difficulty):
    low_range = converted_currency - difficulty
    high_range = converted_currency + difficulty
    if low_range <= user <= high_range:
        result = True
    else:
        result = False
    return result


def play(difficulty):
    secret_number = random.randint(1, 100)
    converted = get_money_interval(secret_number)
    user = get_guess_from_user(secret_number)
    result = compare_results(converted, user, difficulty)
    if result:
        print('Congratulations you win the game! :)')
    else:
        print(f'sorry you lost the game :( it was: {converted} ILS')
    return result
