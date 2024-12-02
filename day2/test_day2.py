import unittest
import time
import numpy as np
from day2 import part1, part2, isSafe, isKindaSafe

class Part1(unittest.TestCase):
    def test1(self):
        res = part1("test1.txt")
        self.assertEqual(res, 2)

class RowsPart1(unittest.TestCase):
    def test1(self):
        input = np.array([7, 6, 4, 2, 1])
        res = isSafe(input)
        self.assertEqual(res, 1)

    def test2(self):
        input = np.array([1, 2, 7, 8, 9])
        res = isSafe(input)
        self.assertEqual(res, 0)

    def test3(self):
        input = np.array([9, 7, 6, 2, 1])
        res = isSafe(input)
        self.assertEqual(res, 0)

    def test4(self):
        input = np.array([1, 3, 2, 4, 5])
        res = isSafe(input)
        self.assertEqual(res, 0)

class RowsPart2(unittest.TestCase):
    def test1(self):
        input = np.array([7, 6, 4, 2, 1])
        res = isKindaSafe(input)
        self.assertEqual(res, 1)

    def test2(self):
        input = np.array([1, 2, 7, 8, 9])
        res = isKindaSafe(input)
        self.assertEqual(res, 0)

    def test3(self):
        input = np.array([9, 7, 6, 2, 1])
        res = isKindaSafe(input)
        self.assertEqual(res, 0)

    def test4(self):
        input = np.array([1, 3, 2, 4, 5])
        res = isKindaSafe(input)
        self.assertEqual(res, 1)

    def test5(self):
        input = np.array([8, 6, 4, 4, 1])
        res = isKindaSafe(input)
        self.assertEqual(res, 1)

class Part2(unittest.TestCase):
    def test1(self):
        res = part2("test1.txt")
        self.assertEqual(res, 4)


if __name__ == '__main__':
    print(part1("input.txt"))
    print()
    print(part2("input.txt"))
    time.sleep(1)
    unittest.main()


