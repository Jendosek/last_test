#13
class Animal:
    pass
class Dog(Animal):
    def make_sound(self):
        print("Собака каже: Гав")
class Cat(Animal):
    def make_sound(self):
        print("Кіт каже: Мяу")
dogi = Dog()
dogi.make_sound()
print()
cat = Cat()
cat.make_sound()
