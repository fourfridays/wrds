import unittest

from polymorphism import Dog, Cat

class TestDog(unittest.TestCase):
    def setUp(self):
        self.dog = Dog()

    def test_is_instance(self):
        self.assertIsInstance(self.dog, Dog)


class TestCat(unittest.TestCase):
    def setUp(self):
        self.cat = Cat()

    def test_is_instance(self):
        self.assertIsInstance(self.cat, Cat)