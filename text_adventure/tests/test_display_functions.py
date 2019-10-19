"""This module contains tests for the elements.display_functions file"""


from text_adventure.tools.display_functions import display


def test_display_method(capsys):
    display("test string")
    out, err = capsys.readouterr()
    assert out == "test string\n"
    assert err == ""
