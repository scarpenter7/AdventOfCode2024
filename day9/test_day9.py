import unittest
import time
import numpy as np
from day9 import part1, part2

class Part1(unittest.TestCase):
    def test1(self):
        res = part1("test1.txt")
        self.assertEqual(res, 1928)

class Part2(unittest.TestCase):
    def test1(self):
        res = part2("test1.txt")
        self.assertEqual(res, 2858)

class Part2_2(unittest.TestCase):
    def test1(self):
        res = part2("test2.txt")
        self.assertEqual(res, 6176)


if __name__ == '__main__':
    start = time.time()
    print(part1("input.txt"))
    print(time.time() - start)
    print()
    start = time.time()
    print(part2("input.txt"))
    print(time.time() - start)
    time.sleep(1)
    unittest.main()


