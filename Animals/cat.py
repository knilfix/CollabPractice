from Animals.animal import Animal


class Cat(Animal):
    def __init__(self, name="Whiskers"):
        super().__init__(name, "Felis catus")

    def speak(self):
        return "Meow!"

    def meow(self):
        return "I can Meow well Now"

    def run(self):
        return "I can Run well now"

    def purr(self):
        return "Purrrrr..."

    def climb(self):
        return f"{self.name} is climbing a tree"

    def die(self):
        return "Cat Died"
