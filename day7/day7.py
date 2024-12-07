
def parse(filename):
    rows = []

    with open(filename) as file:
        for line in file.readlines():
            words = line.split()
            rows.append([int(words[0].split(':')[0])] + [int(n) for n in words[1:]])
    return rows

def part1(filename):
    rows = parse(filename)
    return sum([row[0] for row in rows if isValid(row[0], row[1:])])

def isValid(testVal, nums):
    if len(nums) == 1:
        return nums[0] == testVal
    lastNum = nums[-1]
    divisible = testVal % lastNum == 0
    results = [isValid(testVal - lastNum, nums[:-1])]
    if divisible:
        results.append(isValid(testVal // lastNum, nums[:-1]))
    return any(results)

def part2(filename):
    rows = parse(filename)
    return sum([row[0] for row in rows if isValid2(row[0], row[1:])])

def isValid2(testVal, nums):
    if testVal < 0: return False
    if len(nums) == 1:
        return 0 <= testVal == nums[0]
    lastNum = nums[-1]
    divisible = testVal % lastNum == 0
    matchLastDigits = str(lastNum) == str(testVal)[-len(str(lastNum)):] and testVal != lastNum # last digits match but are not exactly the same numbers
    results = [isValid2(testVal - lastNum, nums[:-1])]
    if divisible:
        results.append(isValid2(testVal // lastNum, nums[:-1]))
    if matchLastDigits:
        newTestNum = int(str(testVal)[:-len(str(lastNum))])
        results.append(isValid2(newTestNum, nums[:-1]))
    return any(results)

def getNextTarget(testVal, lastNum):
    return int(str(testVal)[:-len(str(lastNum))])