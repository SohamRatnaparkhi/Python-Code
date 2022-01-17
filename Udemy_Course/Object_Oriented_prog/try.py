'''
class Boy():
    gender = 'male'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self, game):
        #game = "football"
        print("Hi"+ self.name,game)

obj = Boy(name = "Soham",age = 18)
print(obj.name)
print(obj.age)
print(obj.gender)
print(obj.speak("football"))

class Animal():
    def __init__(self):
        print("Animal")
    def ask_name(self):
        name = input("What's your name? ")
        return name

class Dog(Animal):  #abstract class
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def speak(self, name = "Mr. Dog"):
        print(name + " knows how to bark!")
class Cat(Animal):
    def __init__(self):
        print("Cat Created")
        Animal.__init__(self)
    def speak(self, name = "Mrs. Cat"):
        print(name + " knows how to meow!")
#inheritance is being used
dog = Dog()
cat = Cat()

name_dog = dog.ask_name()
dog.speak(name_dog)

name_cat = cat.ask_name()
cat.speak(name_cat)
#polymorphism is being used
for pet in [dog, cat]:
    print(type(pet))
    print(pet.speak())
'''
from colorama import init
init()
from colorama import Fore
print(Fore.GREEN + "GREEN")
