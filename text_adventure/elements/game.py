"""This file contains the implementation of the Game class."""

from ..tools.output_functions import display, clear_screen
from ..tools.input_functions import collect_input


class Game():
    """The Game class"""

    def __init__(self):
        """Instantiate a game object"""
        clear_screen()

    def main_menu(self):
        display("WORKING TITLE")
        display("> New Game", 0.03)
        display("> Load Game", 0.03)
        display("> Quit", 0.03)
