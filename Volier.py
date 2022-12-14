from BaseAnimal import *
class Volier:
    def __init__(self, name, biom, place):
        self._name = name
        self._biom = biom
        self._place = place
        self._value = 0
        self._list = []

    def addAnimal(self):
        self._list.append(self)

    #def doSound(self):





