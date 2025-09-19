from farm import Farm
from Animals.cat import Cat
from Animals.dog import Dog

# Create farm and animals
my_farm = Farm()
my_farm.add_animal(Cat("Whiskers"))
my_farm.add_animal(Dog("Buddy"))

print("Farm sounds:", my_farm.make_sounds())
