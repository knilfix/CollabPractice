from Animals.animal import Animal

class Dog(Animal):
    def __init__(self, name="Buddy"):
        super().__init__(name, "Canis familiaris")

    def speak(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching a stick"

    def wag_tail(self):
        return f"{self.name}'s tail is wagging happily"
    
    
if __name__ == "__main__":
    dog = Dog("Ralph")
    print(dog.speak())
