import numpy as np
import itertools

def parse(filename):
    rows = []
    charsdict = {}

    with open(filename) as file:
        for i, line in enumerate(file.readlines()):
            words = [char for char in line.strip()]
            rows.append(words)
            for j, char in enumerate(words):
                if char == ".":
                    continue
                if char in charsdict.keys():
                    charsdict[char].append((i, j))
                else:
                    charsdict[char] = [(i, j)]
    return np.array(rows), charsdict

def part1(filename):
    grid, charsdict = parse(filename)
    gridRows = len(grid)
    gridCols = len(grid[0])

    return len(set(itertools.chain(*[getAnomalies(indices, gridRows, gridCols) for indices in charsdict.values()])))

def getAnomalies(indices, gridRows, gridCols):
    combos = list(itertools.combinations(indices, 2))
    anomalies = list(itertools.chain(*[calculateAnomalyIndices(combo, gridRows, gridCols) for combo in combos]))
    return anomalies

def calculateAnomalyIndices(combo, gridRows, gridCols):
    pt1 = combo[0]
    pt2 = combo[1]
    height = pt1[0] - pt2[0]
    width = pt1[1] - pt2[1]
    anomaly1 = (pt1[0] + height, pt1[1] + width)
    anomaly2 = (pt2[0] - height, pt2[1] - width)
    anomaly1Valid = 0 <= anomaly1[0] < gridRows and 0 <= anomaly1[1] < gridCols
    anomaly2Valid = 0 <= anomaly2[0] < gridRows and 0 <= anomaly2[1] < gridCols
    if anomaly1Valid and anomaly2Valid:
        return [anomaly1, anomaly2]
    elif anomaly1Valid:
        return [anomaly1]
    elif anomaly2Valid:
        return [anomaly2]
    return []

def part2(filename):
    grid, charsdict = parse(filename)
    gridRows = len(grid)
    gridCols = len(grid[0])

    return len(set(itertools.chain(*[getAnomalies2(indices, gridRows, gridCols) for indices in charsdict.values()])))

def getAnomalies2(indices, gridRows, gridCols):
    combos = list(itertools.combinations(indices, 2))
    anomalies = list(itertools.chain(*[calculateAnomalyIndices2(combo, gridRows, gridCols) for combo in combos]))
    return anomalies

def calculateAnomalyIndices2(combo, gridRows, gridCols):
    pt1 = combo[0]
    pt2 = combo[1]
    height = pt1[0] - pt2[0]
    width = pt1[1] - pt2[1]
    anomalies = []
    currPt = pt1
    while 0 <= currPt[0] < gridRows and 0 <= currPt[1] < gridCols:
        anomalies.append(currPt)
        currPt = (currPt[0] + height, currPt[1] + width)
    currPt = pt2
    while 0 <= currPt[0] < gridRows and 0 <= currPt[1] < gridCols:
        anomalies.append(currPt)
        currPt = (currPt[0] - height, currPt[1] - width)
    return list(set(anomalies))