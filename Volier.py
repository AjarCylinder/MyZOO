from BaseAnimal import *
class Volier:
    def __init__(self, name, biom, place):
        self._name = name
        self._biom = biom
        self._place = place
        self._list = []
        self._typeOfPredator = ""

    def addAnimal(self, animal):
        if not self._list:  # если список пуст:
            if animal.predator == True:
                if animal.biom == self._biom:
                    if animal.place <= self._place:
                        self._typeOfPredator = animal.typeOfAnimal
                        self._list.append(animal)
                        self._place -= animal.place
                    else:
                        print(animal.name, ":", "мало места")
                else:
                    print(animal.name, ":", "Биом не подходит")
            else:   # predator == false
                if animal.biom == self._biom:
                    if animal.place <= self._place:
                        self._list.append(animal)
                        self._place -= animal.place
                    else:
                        print(animal.name, ":", "мало места")
                else:
                    print(animal.name, ":", "Биом не подходит")
        else:   # список не пустой:
            if animal.predator == True:
                if self._typeOfPredator == animal.typeOfAnimal:
                    if animal.biom == self._biom:
                        if animal.place <= self._place:
                            self._list.append(animal)
                            self._place -= animal.place
                        else:
                            print(animal.name, ":", "мало места")
                    else:
                        print(animal.name, ":", "Биом не подходит")
                else:
                    print(animal.name, ":", "Я охотник, а они нет")
            else:   # predator False
                if animal.biom == self._biom:
                    if animal.place <= self._place:
                        self._list.append(animal)
                        self._place -= animal.place
                    else:
                        print(animal.name, ":", "мало места")
                else:
                    print(animal.name, ":", "Биом не подходит")

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
        return mass

    def seeEat(self, mass):
        if mass > 0:
            print("В вольере осталось", mass)


    @property
    def list(self):
        return self._list

    @property
    def place(self):
        return self._place

    '''if animal.predator == False:
        if animal.biom == self._biom:
            if animal.place <= self._place:
                self._list.append(animal)
                self._place -= animal.place
            else:
                print(animal.name, ":", "mne ne xvataet mesta")
        else:
            print(animal.name, ":", "menya tuda nelza")
    '''