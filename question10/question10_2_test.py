import unittest
import os
from collections import defaultdict
from .question10_2 import BalanceBots


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        input_file = "question10/input.txt"
        with open(input_file) as f:
            instructions = [w.strip() for w in f.read().split('\n')]
        self.code_obj = BalanceBots(instructions)

    def test_balanceBots(self):
        result = self.code_obj.handle_robot()
        self.assertEqual(result, 2666)
