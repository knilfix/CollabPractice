from Animals.animal import Animal


class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Gallus gallus domesticus")

    def speak(self):
        return "Cluck cluck!"

    def lay_egg(self):
        return f"{self.name} laid an egg!"


if __name__ == "__main__":
    pass
