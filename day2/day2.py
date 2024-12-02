import numpy as np

def parse(filename):
    grid = []

    with open(filename) as file:
        for line in file.readlines():
            nums = [int(n) for n in line.split()]
            grid.append(nums)
    return np.array(grid)

def part1(filename):
    grid = parse(filename)
    return sum([isSafe(row) for row in grid])

def is_monotonic(arr):
    diffs = np.diff(arr)
    return np.all(diffs >= 0) or np.all(diffs <= 0)

def isSafe(row):
    if not is_monotonic(row):
        return False
    diffs = np.abs(np.diff(row))
    min_value = 1
    max_value = 3
    return np.all((diffs >= min_value) & (diffs <= max_value))

def part2(filename):
    grid = parse(filename)
    return sum([isKindaSafe(row) for row in grid])

def isKindaSafe(row):
    if isSafe(row):
        return True
    subrows = np.array([np.delete(row, i) for i in range(len(row))])
    return np.any(np.array([isSafe(subrow) for subrow in subrows]))