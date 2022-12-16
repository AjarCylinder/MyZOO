from Elephant import *
from tiger import *
from Volier import *

egor = Tiger("Egor", 5, 15, ["мясо"])
Max = Elephant("Max", 6, 20, ["сено"])
D = Elephant("D", 6, 20, ["сено"])
F = Elephant("F", 6, 20, ["сено"])

volier = Volier("Volier_Elephant", "savannah", 300)

volier.addAnimal(egor)
volier.addAnimal(Max)
volier.addAnimal(D)
volier.addAnimal(F)

volier.doSound()