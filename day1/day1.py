import bisect

def parse(filename):
    arr1, arr2 = [], []

    with open(filename) as file:
        for line in file.readlines():
            words = line.split()
            bisect.insort(arr1, int(words[0]))
            bisect.insort(arr2, int(words[1]))
    return arr1, arr2

def part1(filename):
    arr1, arr2 = parse(filename)
    return sum([abs(a - b) for (a, b) in zip(arr1, arr2)])

def part2(filename):
    arr1, arr2 = parse(filename)
    return sum([a*arr2.count(a) for a in arr1])