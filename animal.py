class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")

    def move(self):
        return f"{self.name} is moving"

    def die(self):
        return f"{self.name} the {self.species} has died"

    def __str__(self):
        return f"{self.name} ({self.species})"
