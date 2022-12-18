class BaseAnimal:
    def __init__(self, name, food_day, age, whatEat):
        self._name = name
        self.food_day = food_day
        self._age = age

        self._biom = ""
        self._place = 0
        self._whatEat = whatEat
        self._predator = True
        self._sound = ""
        self._isFeeded = False
        self._typeOfAnimal = ""

    def doSound(self):
        print(self._name, ":", self._sound)

    def eats(self, mass, typeOfFood):
        if typeOfFood in self.whatEat:
            print(self._name, ": Ya pokushal")
            if mass >= self.food_day:
                self.isFeeded = True
                return self.isFeeded
            else:
                return self.isFeeded
        else:
            print(self._name, ": Ya ne budu eto est'")

    def doPlay(self):
        print(self._name, ": Davai poigrayem!")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value == int:
            self._age = value
        else:
            print("Одумайся, так нельзя")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def place(self):
        return self._place

    @property
    def biom(self):
        return self._biom

    @property
    def predator(self):
        return self._predator

    @property
    def sound(self):
        return self._sound

    @property
    def whatEat(self):
        return self._whatEat


