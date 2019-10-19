"""Classes for items in the game world."""

class Item():
    """The default item class."""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.description}"