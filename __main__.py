"""A command line text adventure written in Python."""

from .tools.display_methods import display
from .elements.locations import Location

a = Location("place", "a place", (0, 0, 0), [])
display("Hello World!")
