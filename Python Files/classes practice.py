class Person:
    def __init__(self, x):
        self.name = x
    def talk(self):
        print('talk')

john = Person("John Smith")
john.talk()
print(john.name)
