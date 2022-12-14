from BaseAnimal import *
class Penguin(BaseAnimal):
    def __init__(self, name, food_day, age, whatEat):
        super().__init__(name, food_day, age, whatEat)
        self.__biom = "tundra"
        self.__place = 16
        self.__whatEat = whatEat
        self.__predator = True
        self.__sound = "Peeek"

