from models import Animal, Dog, Cat
dog = Dog("Rex", 5, "Brown", "Labrador")
cat = Cat("Mimi", 3, "White", 9)
animal = Animal("Generic", 2, "Gray")
animals = [dog, cat, animal]

for a in animals:
    print(a)
    print(a.info())
    print(a.speak())
    print()