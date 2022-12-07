class Elephant:

    def __init__(self, name, food_day, age, whatEat):
        self.name = name
        self.food_day = food_day
        self.age = age

        self.biom = "savannah"
        self.place = "120 m^2"
        self.whatEat = whatEat
        self.predator = False
        self.sound = "UUHHErrrrrrrrrrrRRRRRRRR"
        self.isFeeded = False

    def doSound(self):
        print(self.name, ":", self.sound)

    def eats(self, mass, typeOfEat):
        if (typeOfEat in self.whatEat):
            print(self.name, ": Ya pokushal")
            if mass >= self.food_day:
                self.isFeeded = True
                return self.isFeeded
            else:
                return self.isFeeded
        else:
            print(self.name, ": Ya ne budu eto est'")

    def doPlay(self):
        print(self.name, ": Davai poigrayem!")


class Penguin:
    def __init__(self, name, food_day, age, whatEat):
        self.name = name
        self.food_day = food_day
        self.age = age

        self.biom = "tundra"
        self.place = "16 m^2"
        self.whatEat = whatEat
        self.predator = True
        self.sound = "Peeek"
        self.isFeeded = False

    def doSound(self):
        print(self.name, ":", self.sound)

    def eats(self, mass, typeOfEat):
        if (typeOfEat in self.whatEat):
            print(self.name, ": Ya pokushal")
            if mass >= self.food_day:
                self.isFeeded = True
                return self.isFeeded
            else:
                return self.isFeeded
        else:
            print(self.name, ": Ya ne budu eto est'")

    def doPlay(self):
        print(self.name, ": Davai poigrayem!")


class Tiger:
    def __init__(self, name, food_day, age, whatEat):
        self.name = name
        self.food_day = food_day
        self.age = age

        self.biom = "forest"
        self.place = "20 m^2"
        self.whatEat = whatEat
        self.predator = True
        self.sound = "ROAAARRRR"
        self.isFeeded = False

    def doSound(self):
        print(self.name, ":", self.sound)

    def eats(self, mass, typeOfEat):
        if (typeOfEat in self.whatEat):
            print(self.name, ": Ya pokushal")
            if mass >= self.food_day:
                self.isFeeded = True
                return self.isFeeded
            else:
                return self.isFeeded
        else:
            print(self.name, ": Ya ne budu eto est'")

    def doPlay(self):
        print(self.name, ": Davai poigrayem!")
