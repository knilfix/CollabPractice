from animal import Animal


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Canis lupus familiaris")

    def speak(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball"

    def wag_tail(self):
        return "Tail wagging happily!"


if __name__ == "__main__":
    dog = Dog("Ralph")
    print(dog.speak())
