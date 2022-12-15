from brain_games.game_starter import starter
from brain_games.games.brain_progression import get_game_progression


def main():
    starter(get_game_progression)


if __name__ == "__main__":
    main()
