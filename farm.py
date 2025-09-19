from Animals.cat import Cat
from Animals.cow import Cow
from Animals.dog import Dog
from Animals.chicken import Chicken


class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, index):
        if 0 <= index < len(self.animals):
            return self.animals.pop(index)
        return None

    def list_animals(self):
        if not self.animals:
            return "No animals on the farm yet."
        
        result = f"Animals at {self.name}:\n"
        for i, animal in enumerate(self.animals, 1):
            result += f"{i}. {animal}\n"
        return result

    def make_sounds(self):
        if not self.animals:
            return "The farm is quiet... too quiet."
        
        result = "The farm comes alive with sounds:\n"
        for animal in self.animals:
            result += f"{animal.name}: {animal.speak()}\n"
        return result

    def daily_activities(self):
        if not self.animals:
            return "No animals to perform activities."
        
        activities = []
        for animal in self.animals:
            if isinstance(animal, Chicken):
                activities.append(animal.lay_egg())
            elif isinstance(animal, Dog):
                activities.append(animal.fetch())
            elif isinstance(animal, Cow):
                activities.append(animal.give_milk())
            elif isinstance(animal, Cat):
                activities.append(animal.climb())
        
        result = "Daily activities on the farm:\n"
        for activity in activities:
            result += f"• {activity}\n"
        return result

    def animal_count(self):
        count = {}
        for animal in self.animals:
            species = animal.species
            count[species] = count.get(species, 0) + 1
        return count
