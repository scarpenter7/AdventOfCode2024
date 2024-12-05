
def parse(filename):
    rules = {}
    updates = []

    with open(filename) as file:
        for line in file.readlines():
            if '|' in line:
                pageNums = line.strip().split('|')
                pageNum1 = int(pageNums[0])
                pageNum2 = int(pageNums[1])
                if pageNum1 not in rules.keys():
                    rules[pageNum1] = {pageNum2}
                else:
                    rules[pageNum1].add(pageNum2)
            elif ',' in line:
                update = [int(pageNum) for pageNum in line.strip().split(',')]
                updates.append(update)

    return rules, updates

def part1(filename):
    rules, updates = parse(filename)
    return sum([getMiddle(update) for update in updates if isValid(update, rules)])

def getMiddle(list):
    return list[len(list) // 2]

def isValid(update, rules):
    for i, num in enumerate(update):
        if num not in rules.keys():
            continue
        prevNums = update[:i]
        if any([n in rules[num] for n in prevNums]):
            return False
    return True

def part2(filename):
    rules, updates = parse(filename)
    return sum([reOrder(update, rules) for update in updates if not isValid(update, rules)])

def reOrder(update, rules):
    reorderedUpdate = update.copy()
    while not isValid(reorderedUpdate, rules):
        for i, num in enumerate(reorderedUpdate[::-1]): # iterate in reverse order
            if num not in rules.keys():
                continue
            prevNums = reorderedUpdate[:len(update) - i - 1]
            numsOutOfOrder = [n for n in prevNums if n in rules[num]]
            for numOutOfOrder in numsOutOfOrder:
                reorderedUpdate.remove(numOutOfOrder)
                reorderedUpdate.append(numOutOfOrder)
    return getMiddle(reorderedUpdate)