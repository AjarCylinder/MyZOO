from Elephant import *
from tiger import *
from Volier import *

egor = Tiger("Egor", 5, 15, ["мясо"])
Max = Elephant("Max", 6, 20, ["сено"])
D = Elephant("D", 6, 20, ["сено"])
Bloba = Elephant("Bloba", 6, 20, ["сено"])

volier = Volier("Volier_Elephant", "savannah", 300)

volier.addAnimal(egor)
volier.addAnimal(Max)
volier.addAnimal(Bloba)
volier.addAnimal(D)

volier.feed(11, "сено")

volier.seeEat()

volier.seeAnimalWhoNotEat()

