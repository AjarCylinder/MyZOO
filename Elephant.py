from BaseAnimal import *
class Elephant(BaseAnimal):
    def __init__(self, name, food_day, age, whatEat):
        super().__init__(name, food_day, age, whatEat)

        self.__biom = "savannah"
        self.__place = 120
        self.__whatEat = whatEat
        self.__predator = False
        self.__sound = "UUErrrrrrrrrrrRRRRRRRR"