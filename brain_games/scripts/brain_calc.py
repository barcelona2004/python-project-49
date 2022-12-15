from brain_games.game_starter import starter
from brain_games.games.brain_calc import get_game_calc


def main():
    starter(get_game_calc)


if __name__ == '__main__':
    main()
