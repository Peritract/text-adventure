"""This module contains tests for the elements.game.py file."""

from unittest import mock
from text_adventure.elements.game import Game


@mock.patch('text_adventure.elements.game.display')
def test_game_main_menu(mock_display):
    test_obj = Game()
    test_obj.main_menu()
    assert len(mock_display.mock_calls) == 4
