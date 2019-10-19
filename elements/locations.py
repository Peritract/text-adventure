class Location():
    def __init__(self, name, description, coordinates, exits=[]):
        self.name = name
        self.description = description
        self.coordinates = coordinates
        self.exits = exits
        
    def __str__(self):
        return f"{self.name} - {self.description}"
