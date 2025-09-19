import time
from Animals.cat import Cat
from Animals.chicken import Chicken
from Animals.cow import Cow
from Animals.dog import Dog
from farm import Farm


def print_header(text):
    print("\n" + "="*60)
    print(f" {text} ".center(60, "~"))
    print("="*60)

def animate_text(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def create_animal():
    print_header("ADD ANIMAL TO FARM")
    print("1. Cat")
    print("2. Dog")
    print("3. Cow")
    print("4. Chicken")
    
    try:
        choice = int(input("\nChoose animal type (1-4): "))
        name = input("Enter animal name: ").strip() or None
        
        if choice == 1:
            return Cat(name) if name else Cat()
        elif choice == 2:
            return Dog(name) if name else Dog()
        elif choice == 3:
            return Cow(name) if name else Cow()
        elif choice == 4:
            return Chicken(name) if name else Chicken()
        else:
            print("Invalid choice. Creating a default cat.")
            return Cat()
    except ValueError:
        print("Invalid input. Creating a default cat.")
        return Cat()

def main():
    farm = Farm("Pythonic Pastures")
    
    # Add some initial animals
    farm.add_animal(Cat("Whiskers"))
    farm.add_animal(Dog("Rex"))
    farm.add_animal(Cow("Daisy"))
    farm.add_animal(Chicken("Feathers"))
    
    welcome_message = f"Welcome to {farm.name} Management System!"
    animate_text(welcome_message, 0.02)
    
    while True:
        print_header("MAIN MENU")
        print("1. List all animals")
        print("2. Add an animal")
        print("3. Remove an animal")
        print("4. Listen to animal sounds")
        print("5. View daily activities")
        print("6. Show farm statistics")
        print("7. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-7): "))
            
            if choice == 1:
                print_header("ANIMALS ON THE FARM")
                print(farm.list_animals())
                
            elif choice == 2:
                animal = create_animal()
                result = farm.add_animal(animal)
                print(f"\n{result}")
                
            elif choice == 3:
                print_header("REMOVE ANIMAL FROM FARM")
                print(farm.list_animals())
                if farm.animals:
                    try:
                        index = int(input("\nEnter the number of the animal to remove: ")) - 1
                        result = farm.remove_animal(index)
                        print(result)
                    except ValueError:
                        print("Please enter a valid number.")
                
            elif choice == 4:
                print_header("ANIMAL SOUNDS")
                animate_text(farm.make_sounds())
                
            elif choice == 5:
                print_header("DAILY ACTIVITIES")
                animate_text(farm.daily_activities())
                
            elif choice == 6:
                print_header("FARM STATISTICS")
                count = farm.animal_count()
                print(f"Total animals: {len(farm.animals)}")
                for species, num in count.items():
                    print(f"{species}: {num}")
                    
            elif choice == 7:
                goodbye_message = "Thank you for managing Pythonic Pastures. Goodbye!"
                animate_text(goodbye_message, 0.02)
                break
                
            else:
                print("Please enter a number between 1 and 7.")
                
            input("\nPress Enter to continue...")
            
        except ValueError:
            print("Please enter a valid number between 1 and 7.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()