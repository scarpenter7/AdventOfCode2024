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
  return np.all(np.diff(arr) >= 0) or np.all(np.diff(arr) <= 0)

def isSafe(row):
    if not is_monotonic(row):
        return 0
    diffs = np.abs(np.diff(row))
    min_value = 1
    max_value = 3
    if np.any((diffs < min_value) | (diffs > max_value)):
        return 0
    return 1

def part2(filename):
    grid = parse(filename)
    return sum([isKindaSafe(row) for row in grid])

def isKindaSafe(row):
    if isSafe(row):
        return 1
    subrows = np.array([np.delete(row, i) for i in range(len(row))])
    if np.any(np.array([isSafe(subrow) for subrow in subrows])):
        return 1
    return 0