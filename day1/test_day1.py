import unittest
import time
from day1 import part1, part2

class Part1(unittest.TestCase):
    def test1(self):
        res = part1("test1.txt")
        self.assertEqual(res, 11)

class Part2(unittest.TestCase):
    def test1(self):
        res = part2("test1.txt")
        self.assertEqual(res, 31)


if __name__ == '__main__':
    print(part1("day1-1input.txt"))
    print()
    print(part2("day1-2input.txt"))
    time.sleep(1)
    unittest.main()


