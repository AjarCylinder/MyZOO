from BaseAnimal import *
class Penguin(BaseAnimal):
    def __init__(self, name, food_day, age, whatEat):
        super().__init__(name, food_day, age, whatEat)

        self._biom = "tundra"
        self._place = 16
        self._whatEat = whatEat
        self._predator = True
        self._sound = "Peeek"
        self._typeOfAnimal = "Penguin"
