
# Inheritance...
class Animal():

    def __init__(self, fur):
        self.fur = fur

        print('animal created')

    def report(self):
        print('animal')

    def eat(self):
        print('eating')

class Dog(Animal):

    def __init__(self, fur):
        Animal.__init__(self, fur)
        print('dog created')

    def report(self):
        print('I am a dog')

d = Dog('Fuzzy')
print(d.fur)

