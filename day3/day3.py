import re

def parse(filename):
    res = ""
    with open(filename) as file:
        for line in file.readlines():
            res += line
    return res

def part1(filename):
    line = parse(filename)
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
    return sum([getProduct(mulString) for mulString in matches])

def getProduct(mulString):
    nums = re.findall(r"\d{1,3}", mulString)
    return int(nums[0]) * int(nums[1])

def part2(filename):
    line = parse(filename)
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", line)
    enabledProducts = []
    enabled = True
    for match in matches:
        if match == "don't()":
            enabled = False
        elif match == "do()":
            enabled = True
        elif enabled:
            enabledProducts.append(match)
    return sum([getProduct(mulString) for mulString in enabledProducts])