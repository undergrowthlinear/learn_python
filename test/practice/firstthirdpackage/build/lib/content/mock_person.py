# encoding=utf-8

class Person(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return super().__str__() + "\t" + self.name + "\t" + str(self.age)


person = Person('under', 18)
print(person)
