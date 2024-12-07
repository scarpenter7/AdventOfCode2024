import unittest
import time
import numpy as np
from day6 import part1, part2

class Part1(unittest.TestCase):
    def test1(self):
        res = part1("test1.txt")
        self.assertEqual(res, 41)

class Part2(unittest.TestCase):
    def test1(self):
        res = part2("test1.txt")
        self.assertEqual(res, 6)

class Scratch(unittest.TestCase):
    def test1(self):
        myarr = np.arange(36).reshape((6, 6))
        #print(myarr)
        #print(myarr[:3, 2])
        #print(myarr[1:, 2])

if __name__ == '__main__':
    print(part1("input.txt"))
    print()
    start = time.time()
    print(part2("input.txt"))
    print(time.time() - start)
    time.sleep(1)
    unittest.main()


