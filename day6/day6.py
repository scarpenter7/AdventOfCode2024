import numpy as np
import concurrent.futures
from typing import Callable, Any

dirs = ["up", "right", "down", "left"]

def parse(filename):
    grid = []

    with open(filename) as file:
        for line in file.readlines():
            letters = [letter for letter in line.strip()]
            grid.append(np.array(letters, dtype='U1'))
    return np.array(grid)

def part1(filename):
    grid = parse(filename)
    row, col = np.where(grid == '^')
    currRow, currCol = row[0], col[0]
    grid[currRow, currCol] = 'X'
    currDir = 0
    while True:
        currDirStr = dirs[currDir]
        if currDirStr == "up":
            fullPath = grid[:currRow, currCol][::-1]
            distTraveled = getDistTraveled(fullPath)
            grid[currRow - distTraveled:currRow,currCol] = 'X'
            currRow -= distTraveled
        elif currDirStr == "right":
            fullPath = grid[currRow, currCol + 1:]
            distTraveled = getDistTraveled(fullPath)
            grid[currRow, currCol:currCol + distTraveled + 1] = 'X'
            currCol += distTraveled
        elif currDirStr == "down":
            fullPath = grid[currRow + 1:, currCol]
            distTraveled = getDistTraveled(fullPath)
            grid[currRow:currRow + distTraveled + 1, currCol] = 'X'
            currRow += distTraveled
        elif currDirStr == "left":
            fullPath = grid[currRow, :currCol][::-1]
            distTraveled = getDistTraveled(fullPath)
            grid[currRow, currCol - distTraveled:currCol] = 'X'
            currCol -= distTraveled
        if '#' not in fullPath:
            return np.sum(grid == 'X')
        currDir += 1
        currDir %= len(dirs)


def getDistTraveled(fullPath):
    if '#' not in fullPath:
        return np.size(fullPath)
    return np.where(fullPath == '#')[0][0]

def part2(filename):
    grid = parse(filename)
    result = vectorize_with_indices(checkIfLoops)(grid)
    return np.sum(result)

def checkIfLoops(value, obstacleRow, obstableCol, grid):
    if value == '#' or value == '^':
        return False
    gridCopy = grid.copy()
    row, col = np.where(gridCopy == '^')

    currRow, currCol = row[0], col[0]
    gridCopy[obstacleRow, obstableCol] = '#'
    visitedDestinationDirPairs = {(currRow, currCol, 0)}  # started at this location going up
    currDir = 0
    while True:
        currDirStr = dirs[currDir]
        if currDirStr == "up":
            fullPath = gridCopy[:currRow, currCol][::-1]
            distTraveled = getDistTraveled(fullPath)
            currRow -= distTraveled
        elif currDirStr == "right":
            fullPath = gridCopy[currRow, currCol + 1:]
            distTraveled = getDistTraveled(fullPath)
            currCol += distTraveled
        elif currDirStr == "down":
            fullPath = gridCopy[currRow + 1:, currCol]
            distTraveled = getDistTraveled(fullPath)
            currRow += distTraveled
        elif currDirStr == "left":
            fullPath = gridCopy[currRow, :currCol][::-1]
            distTraveled = getDistTraveled(fullPath)
            currCol -= distTraveled
        if '#' not in fullPath:
            return False
        currDir += 1
        currDir %= len(dirs)
        visitedStop = (currRow, currCol, currDir)
        if visitedStop in visitedDestinationDirPairs:
            return True
        visitedDestinationDirPairs.add(visitedStop)


def vectorize_with_indices(func: Callable[[Any, int, int, np.ndarray], Any]):

    def wrapper(arr: np.ndarray) -> np.ndarray:
        # Create a result array with the same shape as input
        result = np.zeros_like(arr, dtype=float)

        # Determine the number of cores to use
        max_workers = min(8, arr.shape[0] * arr.shape[1])  # Cap at 8, or total elements

        # Use ThreadPoolExecutor for I/O-bound or NumPy/SciPy operations
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Prepare futures for each element
            futures = {}
            for row in range(arr.shape[0]):
                for col in range(arr.shape[1]):
                    # Submit each element transformation as a separate task
                    # Pass the entire array along with element and indices
                    future = executor.submit(func, arr[row, col], row, col, arr)
                    futures[(row, col)] = future

            # Collect results
            for (row, col), future in futures.items():
                result[row, col] = future.result()

        return result

    return wrapper
