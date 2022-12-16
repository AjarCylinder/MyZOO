from BaseAnimal import *
class Volier:
    def __init__(self, name, biom, place):
        self._name = name
        self._biom = biom
        self._place = place
        self._list = []

    def addAnimal(self, animal):
        if animal.biom == self._biom:
            if animal.place < self._place:
                self._list.append(animal)
                self._place += animal.place
            else:
                print(animal.name, ":", "mne ne xvataet mesta")
        else:
            print(animal.name, ":", "menya tuda nelza")

    def deleteAnimal(self, animal):
        self._list.remove(animal)

    def doSound(self):
        for i in self._list:
            i.doSound()

    def feed(self, mass, typeOfFood):
        for i in self._list:
            if typeOfFood in i.whatEat:
                if mass > i.food_day:
                    i.eats(i.food_day, typeOfFood)
                    mass -= i.food_day
                else:
                    print(i.name, ":", "mne ne xvativo")
            else:
                print(i.name, ":", "ya takoe ne em")

    @property
    def list(self):
        return self._list

    @property
    def place(self):
        return self._place