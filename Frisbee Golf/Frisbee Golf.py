"""
Import dependencies
"""
from Initialise import *
from Utilities import *

# startup graphic
show_pic("Map\Intro.jpg")
print("Welcome to Nick's Frisbee Golf Challenge")


TheGame = construct_game()

# set up players
TheGame.setup_players()

# sets up characters
TheGame.setup_characters()


TheGame.play()
