
def parse(filename):
    rows = []

    with open(filename) as file:
        for line in file.readlines():
            words = line.split()
            rows.append(words)
    return rows

def part1(filename):
    rows = parse(filename)
    return 0

def part2(filename):
    rows = parse(filename)
    return 0