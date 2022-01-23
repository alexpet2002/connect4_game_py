import utilities
from utilities import *

if __name__ == '__main__':
    # imports

    # Declared variables
    utilities.scores_of_players = scores(0, 0)
    utilities.first_players_turn = True
    utilities.continue_playing = True
    utilities.try_again = True

    # Initialization
    intialize_matrix()

    # Main Game
    game_loop()

    # End program
    ending_message()
