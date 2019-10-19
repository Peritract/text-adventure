"""A command line text adventure written in Python."""

from .tools.display_methods import display
from .elements.locations import Location

# hacks to test concepts - will be replaced when there is real functionality
a = Location("place", "a place", (0, 0, 0), [])
display(a.__str__())
print(a)
