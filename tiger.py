from BaseAnimal import *

class Tiger(BaseAnimal):
    def __init__(self, name, food_day, age, whatEat):
        super().__init__(name, food_day, age, whatEat)
        self._biom = "forest"
        self._place = "20 m^2"
        self._whatEat = whatEat
        self._predator = True
        self._sound = "ROAAARRRR"
        self.isFeeded = False


