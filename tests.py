import unittest
from BaseAnimal import *
from tiger import *
from Elephant import *
from penguin import *
from Volier import *

class Volier_test(unittest.TestCase):
    def setUp(self):
        self.Volier = Volier("v1", "savannah", 500)

    def test_AddAnimal(self):
        expected = 1
        elephant = Elephant("grigoriy",5,12,'сено')
        self.Volier.addAnimal(elephant)
        actual = len(self.Volier.list)
        self.assertEqual(expected, actual)

    def test_deleteAnimal(self):
        expected = 0
        elephant = Elephant("grigoriy", 5, 12, 'сено')
        self.Volier.addAnimal(elephant)
        self.Volier.deleteAnimal(elephant)
        actual = len(self.Volier.list)
        self.assertEqual(expected, actual)

    def test_feed_p(self):
        expected = 2
        elephant = Elephant("grigoriy", 5, 12, 'сено')
        elephant1 = Elephant("gosha", 5, 12, 'сено')
        self.Volier.addAnimal(elephant)
        self.Volier.addAnimal(elephant1)
        actual = self.Volier.feed(10,"сено")
        self.assertEqual(expected, actual)

    def test_feed_np(self):
        expected = 1
        elephant = Elephant("grigoriy", 5, 12, 'сено')
        elephant1 = Elephant("gosha", 5, 12, 'сено')
        elephant2 = Elephant("efgesha", 5, 12, 'сено')
        self.Volier.addAnimal(elephant)
        self.Volier.addAnimal(elephant1)
        self.Volier.addAnimal(elephant2)
        actual = len(self.Volier.list) - self.Volier.feed(10,"сено")
        self.assertEqual(expected, actual)

class BaseAnimal_Test(unittest.TestCase):
    def test_eats(self):
        expected = True
        elephant = Elephant("grigoriy", 5, 12, 'сено')
        actual = elephant.eats(6, "сено")
        self.assertEqual(expected, actual)