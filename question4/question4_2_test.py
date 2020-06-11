import unittest
from .question4_2 import SecurityThroughObscurity


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        input_file = "question4/input.txt"
        with open(input_file) as f:
            instructions = [w.strip() for w in f.read().split('\n')]
        self.obj = SecurityThroughObscurity(instructions)

    def test_securityThroughObscurity(self):
        self.assertEqual(self.obj.find_sector_id(), 482)


if __name__ == '__main__':
    unittest.main()
