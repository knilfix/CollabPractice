from Animals.cat import Cat
from Animals.dog import Dog
from Animals.chicken import Chicken


class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def make_sounds(self):
        return [animal.speak() for animal in self.animals]

    def daily_activities(self):
        activities = []
        for animal in self.animals:
            if hasattr(animal, "lay_egg"):
                activities.append(animal.lay_egg())
            elif hasattr(animal, "fetch"):
                activities.append(animal.fetch())
        return activities
