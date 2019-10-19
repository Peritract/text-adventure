"""This module contains tests for the tools.output_functions file"""

from unittest import mock
import sys

from text_adventure.tools.output_functions import display, clear_screen


def test_display_function(capsys):
    """Tests that the display function outputs as expected."""
    display("test string")
    out, err = capsys.readouterr()
    assert out == "test string\n"
    assert err == ""


@mock.patch("os.system")
def test_clear_screen_function(mock_os):
    """Tests that clear_screen calls os.system as expected"""
    clear_screen()
    if sys.platform == 'win32':
        assert mock_os.called_with("cls")
    else:
        assert mock_os.called_with("clear")
    assert mock_os.called_once()
