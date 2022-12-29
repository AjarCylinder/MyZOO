from BaseAnimal import *
class Volier:
    def __init__(self, name, biom, place):
        self._name = name
        self._biom = biom
        self._place = place
        self._list = []
        self._typeOfPredator = ""
        self._massOfFood = 0
        self.typeOfFood = ""
        self._listWhoNotEat = []

    def addAnimal(self, animal):
        if not self._list:  # если список пуст:
            if animal.predator == True:
                if animal.biom == self._biom:
                    if animal.place <= self._place:
                        self._typeOfPredator = animal.typeOfAnimal
                        self._list.append(animal)
                        self._place -= animal.place
                        print("Животное подселено!")
                    else:
                        print(animal.name, ":", "мало места")
                else:
                    print(animal.name, ":", "Биом не подходит")
            else:   # predator == false
                if animal.biom == self._biom:
                    if animal.place <= self._place:
                        self._list.append(animal)
                        self._place -= animal.place
                        print("Животное подселено!")
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
                            print("Животное подселено!")
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
                        print("Животное подселено!")
                    else:
                        print(animal.name, ":", "мало места")
                else:
                    print(animal.name, ":", "Биом не подходит")

    def deleteAnimal(self, animal):
        self._list.remove(animal)
        print("Животное отселено!")

    def doSound(self):
        for i in self._list:
            i.doSound()

    def feed(self, mass, typeOfFood):
        p = 0
        np = 0
        self._massOfFood = mass
        self.typeOfFood = typeOfFood
        for i in self._list:
            if self.typeOfFood in i.whatEat:
                if self._massOfFood >= i.food_day:
                    i.eats(i.food_day, self.typeOfFood)
                    self._massOfFood -= i.food_day
                    p += 1
                else:
                    i.food_day -= self._massOfFood
                    print(i.name, ":", "mne ne xvativo")
                    self._massOfFood = 0
                    self._listWhoNotEat.append(i)
                    np += 1
            else:
                print(i.name, ":", "ya takoe ne em")
        return p

    def seeEat(self):
        if self._massOfFood >= 0:
            print("В вольере осталось", self._massOfFood, self.typeOfFood)

    def seeAnimalWhoNotEat(self):
        for i in self._listWhoNotEat:
            print(i.name, ":", "я не наелся, мне нужно ещё", i.food_day, i.whatEat)


    @property
    def list(self):
        return self._list

    @property
    def place(self):
        return self._place

