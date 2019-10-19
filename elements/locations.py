class Location():
    def __init__(self, name, coordinates, exits=[]):
        self.name = name
        self.coordinates = coordinates
        self.exits = exits