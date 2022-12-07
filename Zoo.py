class Elephant:

    def __init__(self, name, food_day, age, whatEat):
        self.__name = name
        self.food_day = food_day
        self.__age = age

        self.__biom = "savannah"
        self.__place = "120 m^2"
        self.__whatEat = whatEat
        self.__predator = False
        self.__sound = "UUHHErrrrrrrrrrrRRRRRRRR"
        self.isFeeded = False

    def doSound(self):
        print(self.__name, ":", self.__sound)

    def eats(self, mass, typeOfEat):
        if (typeOfEat in self.__whatEat):
            print(self.__name, ": Ya pokushal")
            if mass >= self.food_day:
                self.isFeeded = True
                return self.isFeeded
            else:
                return self.isFeeded
        else:
            print(self.__name, ": Ya ne budu eto est'")

    def doPlay(self):
        print(self.__name, ": Davai poigrayem!")

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, value):
        if value == int:
            self.__age = value
        else:
            print("Одумайся, так нельзя")
    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name

    @property
    def place(self):
        return self.__place

    @property
    def biom(self):
        return self.__biom

    @property
    def predator(self):
        return self.__predator

    @property
    def sound(self):
        return self.__sound

    @property
    def whatEat(self):
        return self.__whatEat

class Penguin:
    def __init__(self, name, food_day, age, whatEat):
        self.__name = name
        self.food_day = food_day
        self.__age = age

        self.__biom = "tundra"
        self.__place = "16 m^2"
        self.__whatEat = whatEat
        self.__predator = True
        self.__sound = "Peeek"
        self.isFeeded = False

    def doSound(self):
        print(self.__name, ":", self.__sound)

    def eats(self, mass, typeOfEat):
        if (typeOfEat in self.whatEat):
            print(self.__name, ": Ya pokushal")
            if mass >= self.food_day:
                self.isFeeded = True
                return self.isFeeded
            else:
                return self.isFeeded
        else:
            print(self.__name, ": Ya ne budu eto est'")

    def doPlay(self):
        print(self.__name, ": Davai poigrayem!")

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, value):
        if value == int:
            self.__age = value
        else:
            print("Одумайся, так нельзя")

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name

    @property
    def place(self):
        return self.__place

    @property
    def biom(self):
        return self.__biom

    @property
    def predator(self):
        return self.__predator

    @property
    def sound(self):
        return self.__sound

    @property
    def whatEat(self):
        return self.__whatEat


class Tiger:
    def __init__(self, name, food_day, age, whatEat):
        self.__name = name
        self.food_day = food_day
        self.__age = age

        self.__biom = "forest"
        self.__place = "20 m^2"
        self.__whatEat = whatEat
        self.__predator = True
        self.__sound = "ROAAARRRR"
        self.isFeeded = False

    def doSound(self):
        print(self.__name, ":", self.__sound)

    def eats(self, mass, typeOfEat):
        if (typeOfEat in self.whatEat):
            print(self.__name, ": Ya pokushal")
            if mass >= self.food_day:
                self.isFeeded = True
                return self.isFeeded
            else:
                return self.isFeeded
        else:
            print(self.__name, ": Ya ne budu eto est'")

    def doPlay(self):
        print(self.__name, ": Davai poigrayem!")

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, value):
        if value == int:
            self.__age = value
        else:
            print("Одумайся, так нельзя")

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name

    @property
    def place(self):
        return self.__place

    @property
    def biom(self):
        return self.__biom

    @property
    def predator(self):
        return self.__predator

    @property
    def sound(self):
        return self.__sound

    @property
    def whatEat(self):
        return self.__whatEat
