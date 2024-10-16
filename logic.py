# from logic import repeat_with_remaining_attempts
from decouple import Config, Csv
from configparser import ConfigParser
from hw5 import GuessTheNumber

def main():
    config = ConfigParser()
    config.read('settings.ini')

    min_number = config.getint('game', 'min_number')
    max_number = config.getint('game', 'max_number')
    attempts = config.getint('game', 'attempts')
    initial_capital = config.getint('game', 'initial_capital')

    game = GuessTheNumber(min_number, max_number, attempts, initial_capital)
    game.play_game()

if __name__ == "__main__":
    main()