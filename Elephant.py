from BaseAnimal import *
class Elephant(BaseAnimal):
    def __init__(self, name, food_day, age, whatEat):
        super().__init__(name, food_day, age, whatEat)

        self._biom = "savannah"
        self._place = 120
        self._whatEat = whatEat
        self._predator = False
        self._sound = "UUErrrrrrrrrrrRRRRRRRR"