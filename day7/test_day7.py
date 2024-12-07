import unittest
import time
import numpy as np
from day7 import part1, part2, isValid, isValid2

class Part1(unittest.TestCase):
    def test1(self):
        res = part1("test1.txt")
        self.assertEqual(res, 3749)

class Part2(unittest.TestCase):
    def test1(self):
        res = part2("test1.txt")
        self.assertEqual(res, 11387)

class IsValid(unittest.TestCase):
    def test1(self):
        testNum = 190
        nums = [10, 19]
        res = isValid(testNum, nums)
        self.assertTrue(res)

    def test2(self):
        testNum = 3267
        nums = [81, 40, 27]
        res = isValid(testNum, nums)
        self.assertTrue(res)

    def test3(self):
        testNum = 83
        nums = [17, 5]
        res = isValid(testNum, nums)
        self.assertFalse(res)

    def test4(self):
        testNum = 156
        nums = [15, 6]
        res = isValid(testNum, nums)
        self.assertFalse(res)

    def test5(self):
        testNum = 7290
        nums = [6, 8, 6, 15]
        res = isValid(testNum, nums)
        self.assertFalse(res)

    def test6(self):
        testNum = 161011
        nums = [16, 10, 13]
        res = isValid(testNum, nums)
        self.assertFalse(res)

    def test7(self):
        testNum = 192
        nums = [17, 8, 14]
        res = isValid(testNum, nums)
        self.assertFalse(res)

    def test8(self):
        testNum = 21037
        nums = [9, 7, 18, 13]
        res = isValid(testNum, nums)
        self.assertFalse(res)

    def test9(self):
        testNum = 292
        nums = [11, 6, 16, 20]
        res = isValid(testNum, nums)
        self.assertTrue(res)

class IsValid2(unittest.TestCase):
    def test1(self):
        testNum = 190
        nums = [10, 19]
        res = isValid2(testNum, nums)
        self.assertTrue(res)

    def test2(self):
        testNum = 3267
        nums = [81, 40, 27]
        res = isValid2(testNum, nums)
        self.assertTrue(res)

    def test3(self):
        testNum = 83
        nums = [17, 5]
        res = isValid2(testNum, nums)
        self.assertFalse(res)

    def test4(self):
        testNum = 156
        nums = [15, 6]
        res = isValid2(testNum, nums)
        self.assertTrue(res)

    def test5(self):
        testNum = 7290
        nums = [6, 8, 6, 15]
        res = isValid2(testNum, nums)
        self.assertTrue(res)

    def test6(self):
        testNum = 161011
        nums = [16, 10, 13]
        res = isValid2(testNum, nums)
        self.assertFalse(res)

    def test7(self):
        testNum = 192
        nums = [17, 8, 14]
        res = isValid2(testNum, nums)
        self.assertTrue(res)

    def test8(self):
        testNum = 21037
        nums = [9, 7, 18, 13]
        res = isValid2(testNum, nums)
        self.assertFalse(res)

    def test9(self):
        testNum = 292
        nums = [11, 6, 16, 20]
        res = isValid2(testNum, nums)
        self.assertTrue(res)


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


