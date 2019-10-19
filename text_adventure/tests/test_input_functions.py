"""This module contains tests for the tools.input_functions file"""

from text_adventure.tools.input_functions import clean_input


def test_clean_input_function():
    """Tests that clean_input returns text as expected"""
    assert type(clean_input("a")) == str
    assert clean_input("I saw a horse") == "i saw a horse"
    assert clean_input("XxXxxxX") == "xxxxxxx"
    assert clean_input(" \n road  ") == "road"
