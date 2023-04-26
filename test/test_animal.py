# test_example.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))


from animal import Animal, Dog, Cat

def test_animal():
    animal = Animal("Spot")
    assert animal.name == "Spot"

def test_dog():
    dog = Dog("Rufus", "Labrador")
    assert dog.name == "Rufus"
    assert dog.breed == "Labrador"
    assert dog.speak() == "Woof!"

def test_cat():
    cat = Cat("Whiskers", "Gray")
    assert cat.name == "Whiskers"
    assert cat.color == "Gray"
    assert cat.speak() == "Meow!"