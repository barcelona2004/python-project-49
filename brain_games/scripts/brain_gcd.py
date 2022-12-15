from brain_games.game_starter import starter
from brain_games.games.brain_gcd import get_game_gcd


def main():
    starter(get_game_gcd)


if __name__ == "__main__":
    main()
