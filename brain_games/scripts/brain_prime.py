from brain_games.game_starter import starter
from brain_games.games.brain_prime import get_game_prime


def main():
    starter(get_game_prime)


if __name__ == "__main__":
    main()
