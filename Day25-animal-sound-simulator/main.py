# Day 25 - Animal Sound Simulator
# Concept: Polymorphism
# Goal: Practice how different classes can share the same method name but behave differently

# --- Parent class with a generic method ---
class Animal:

    def __init__(self, name):
        self.name = name

    # --- A method meant to be OVERRIDDEN by every child class ---
    def make_sound(self):
        return "Some generic animal sound"

    def __str__(self):
        return f"{self.name} the {self.__class__.__name__}"


# --- Each child class overrides make_sound() in its OWN way ---
class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Cow(Animal):
    def make_sound(self):
        return "Moo!"


class Duck(Animal):
    def make_sound(self):
        return "Quack!"


# --- Creating one object of each type ---
dog = Dog("Rex")
cat = Cat("Whiskers")
cow = Cow("Bessie")
duck = Duck("Donald")

# --- THIS is polymorphism: same method call, different behavior per object ---
print(f"{dog.name} says: {dog.make_sound()}")
print(f"{cat.name} says: {cat.make_sound()}")
print(f"{cow.name} says: {cow.make_sound()}")
print(f"{duck.name} says: {duck.make_sound()}")

# --- The real power: looping through DIFFERENT types and calling the SAME method ---
# The loop doesn't need to know or care what type each animal actually is
animals = [dog, cat, cow, duck]

print("\n--- Making all animals speak (polymorphism in action) ---")
for animal in animals:
    print(f"{animal} says: {animal.make_sound()}")

# --- A function that works with ANY Animal subclass - doesn't need to know which ---
def animal_chorus(animal_list):
    for animal in animal_list:
        print(animal.make_sound())

print("\n--- Calling a function that works with any Animal ---")
animal_chorus(animals)

# --- Using super() to extend a parent method instead of fully replacing it ---
class Parrot(Animal):
    def make_sound(self):
        # call the parent's version first, then add to it
        generic = super().make_sound()
        return f"{generic}... just kidding, Squawk!"

parrot = Parrot("Polly")
print(f"\n{parrot.name} says: {parrot.make_sound()}")

# --- An object that DOESN'T override make_sound() falls back to the parent's version ---
class UnknownAnimal(Animal):
    pass   # no override at all

mystery = UnknownAnimal("???")
print(f"\n{mystery.name} says: {mystery.make_sound()}")   # uses Animal's generic version

# --- Polymorphism also works with built-in functions like len() ---
# len() behaves differently depending on the object type (str, list, dict, etc.)
# - this is polymorphism too, just built into Python itself
print("\n--- Built-in polymorphism example ---")
print("len('hello'):", len("hello"))
print("len([1, 2, 3]):", len([1, 2, 3]))
print("len({'a': 1, 'b': 2}):", len({"a": 1, "b": 2}))


# ============================================================
# Interactive part: add your own animal and hear its sound
# ============================================================
sound_map = {
    "dog": Dog,
    "cat": Cat,
    "cow": Cow,
    "duck": Duck,
}

print("\n--- Animal Sound Simulator ---")
print("Available types: dog, cat, cow, duck")
animal_type = input("Choose an animal type: ").lower()
animal_name = input("Give it a name: ")

if animal_type in sound_map:
    new_animal = sound_map[animal_type](animal_name)
    animals.append(new_animal)
    print(f"\n{new_animal} says: {new_animal.make_sound()}")
else:
    print("Unknown animal type - using generic Animal instead.")
    new_animal = Animal(animal_name)
    print(f"{new_animal} says: {new_animal.make_sound()}")