from Animals.animal import Animal


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Bos taurus")

    def speak(self):
        return "Moo!"

    def give_milk(self):
        return f"{self.name} is giving milk"
