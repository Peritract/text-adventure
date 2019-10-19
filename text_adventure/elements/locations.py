"""This file contains the implementations of in-game locations."""


class Location():
    """The base location class."""

    def __init__(self, name, description, coordinates, exits=[]):
        """Constructor method for the base location class."""
        self.name = name
        self.description = description
        self.coordinates = coordinates
        self.exits = exits

    def __str__(self):
        """Returns the name & description."""
        return f"{self.name} - {self.description}"
