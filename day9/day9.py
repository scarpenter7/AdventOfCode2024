
def parse(filename):
    rows = None

    with open(filename) as file:
        for line in file.readlines():
            nums = [int(n) for n in line.strip()]
            rows = nums
    return rows

def part1(filename):
    nums = parse(filename)
    wideRepresentation = createWideRepresentation(nums)
    sortedBlocks = sortBlocks(wideRepresentation)
    return sum([i * n for (i, n) in enumerate(sortedBlocks)])

def createWideRepresentation(nums):
    wideRepresentation = []
    idNum = 0
    lengthFile = True
    for num in nums:
        if lengthFile:
            wideRepresentation += [idNum] * num
            idNum += 1
        else:
            wideRepresentation += ['.'] * num
        lengthFile = not lengthFile
    return wideRepresentation

def sortBlocks(arr):
    result = arr.copy()
    numDots = arr.count('.')
    replacementNums = [n for n in arr[::-1] if isinstance(n, int)]
    replacement_index = 0
    for i in range(len(result[:-numDots])):
        if result[i] == '.':
            result[i] = replacementNums[replacement_index]
            replacement_index += 1
    return result[:-numDots]

def part2(filename):
    nums = parse(filename)
    if len(nums) % 2 != 0:
        nums.append(0)
    wideRepresentation = createWideRepresentation(nums)
    blocks = nums[::2]
    gaps = nums[1::2]
    usedGaps = [0] * len(gaps)
    gapTracker = {}

    for i, block in enumerate(blocks[::-1]):
        blockID = len(blocks) - i - 1
        blockIdx = sum(nums[::-1][i * 2 + 1:]) - block
        gapIdx = 0
        while gapIdx < len(gaps) and block > gaps[gapIdx]:
            gapIdx += 1
        if gapIdx < len(gaps):
            wideRepGapIdx = sum(nums[:int(gapIdx * 2) + 1]) + usedGaps[gapIdx]
            if wideRepGapIdx < blockIdx:
                gaps[gapIdx] -= block
                usedGaps[gapIdx] += block
                wideRepresentation[wideRepGapIdx: wideRepGapIdx + block] = [blockID] * block
                eraseIdx = len(wideRepresentation) - sum(nums[::-1][:2 * (i + 1)])
                wideRepresentation[eraseIdx: eraseIdx + block] = ['.'] * block
    return sum([i * n for (i, n) in enumerate(wideRepresentation) if isinstance(n, int)])