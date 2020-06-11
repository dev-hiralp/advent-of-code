import unittest
import os
from .question1_2 import NoTaxicab


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        input_file = "question1/input.txt"
        with open(input_file) as f:
            instructions = [w.strip() for w in f.read().split(',')]
        self.obj = NoTaxicab(instructions)

    def test_notaxicab(self):
        result = self.obj.block_dist_slover()
        self.assertEqual(result, 150)


if __name__ == '__main__':
    unittest.main()
