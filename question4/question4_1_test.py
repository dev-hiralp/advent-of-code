import unittest
import os
from .question4_1 import SecurityThroughObscurity


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        input_file = "question4/input.txt"
        with open(input_file) as f:
            instructions = [w.strip() for w in f.read().split('\n')]
        self.obj = SecurityThroughObscurity(instructions)

    def test_securityThroughObscurity(self):
        self.assertEqual(self.obj.calculate_sum_for_real_rooms(), 361724)


if __name__ == '__main__':
    unittest.main()
