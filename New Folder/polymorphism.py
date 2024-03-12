class Animal:
    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):
        return "Meowww"
    
class Anjing(Animal):
    def speak(self):
        return "Gug Gug"
    
class Bebek(Animal):
    def speak(self):
        return "Kwek Kwek"
    
print(Cat().speak())
print(Anjing().speak())
print(Bebek().speak())