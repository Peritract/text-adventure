"""This file contains functions that accept and process keyboard input."""

from .output_functions import display


def clean_input(text):
    """Converts raw text to a consistent format."""
    return text.lower().strip()


def collect_input(message=None, prompt="> ", valid=[], cast=str):
    """Prompts the user for input."""
    if message:
        display(message)
    raw_input = input(prompt)
