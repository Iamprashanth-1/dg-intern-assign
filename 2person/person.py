from abc import ABC, abstractclassmethod

class Person(ABC):
    @abstractclassmethod

    def get_gender(self):
        pass


class Male(Person):
    def get_gender(self):
        print('MAle')
class Female(Person):
    def get_gender(self):
        print('Female')

d=Male()
d.get_gender()
h=Female()
h.get_gender()