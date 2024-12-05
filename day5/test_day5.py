import unittest
import time
from day5 import part1, part2

class Part1(unittest.TestCase):
    def test1(self):
        res = part1("test1.txt")
        self.assertEqual(res, 143)

class Part2(unittest.TestCase):
    def test1(self):
        res = part2("test1.txt")
        self.assertEqual(res, 123)


if __name__ == '__main__':
    print(part1("input.txt"))
    print()
    print(part2("input.txt"))
    time.sleep(1)
    unittest.main()


