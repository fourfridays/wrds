from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print (f"The Dog said woof.")

class Cat(Animal):
    def speak(self):
        print (f"The Cat said meow.")