"""This module contains tests for the test_display_methods file"""


from .display_methods import display


def test_display_method(capfd):
    display("test string")
    out, err = capfd.readouterr()
    assert out == "test string\n"
    assert err == ""
