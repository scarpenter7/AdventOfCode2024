import numpy as np

def parse(filename):
    grid = []

    with open(filename) as file:
        for line in file.readlines():
            letters = [letter for letter in line.strip()]
            grid.append(np.array(letters, dtype='U1'))
    return np.array(grid)

def part1(filename):
    grid = np.pad(parse(filename), 3, mode='constant', constant_values='O')
    Xs = np.transpose(np.where(grid == 'X'))
    v_func = np.vectorize(findNumXmas, signature='(n,m),(2)->()')
    result_grid = v_func(grid, Xs)
    return np.sum(result_grid)

def findNumXmas(grid, index):
    row, col = index
    words = np.array([
        ''.join(grid[row-3:row, col][::-1]), #up
        ''.join(grid[row, col+1:col+4]), #right
        ''.join(grid[row+1:row+4, col]), #down
        ''.join(grid[row, col-3:col][::-1]), #left
        ''.join(get_diagonal(grid, row-1, col+1, 3, direction="up-right")),
        ''.join(get_diagonal(grid, row+1, col+1, 3, direction="down-right")),
        ''.join(get_diagonal(grid, row-1, col-1, 3, direction="up-left")),
        ''.join(get_diagonal(grid, row+1, col-1, 3, direction="down-left")),
    ])
    return np.size(np.where(words == "MAS"))


def get_diagonal(arr, start_row, start_col, length, direction="up-right"):
    if direction == "up-right":
        # Slice elements going up and to the right
        sliced_arr = arr[start_row - length + 1:start_row + 1, start_col:start_col + length]
        reflected_arr = np.flipud(sliced_arr.T)  # Flip up and transpose to align the diagonal
    elif direction == "down-right":
        # Slice elements going down and to the right
        sliced_arr = arr[start_row:start_row + length, start_col:start_col + length]
        reflected_arr = sliced_arr
    elif direction == "up-left":
        # Slice elements going up and to the left
        sliced_arr = arr[start_row - length + 1:start_row + 1, start_col - length + 1:start_col + 1]
        reflected_arr = np.flipud(np.fliplr(sliced_arr.T))  # Flip both vertically and horizontally
    elif direction == "down-left":
        # Slice elements going down and to the left
        sliced_arr = arr[start_row:start_row + length, start_col - length + 1:start_col + 1]
        reflected_arr = np.fliplr(sliced_arr)

    # Extract the diagonal
    if direction == "up-right":
        return reflected_arr.diagonal()[::-1]
    return reflected_arr.diagonal()

def part2(filename):
    grid = np.pad(parse(filename), 1, mode='constant', constant_values='O')
    Xs = np.transpose(np.where(grid == 'A'))
    v_func = np.vectorize(findNumMas, signature='(n,m),(2)->()')
    result_grid = v_func(grid, Xs)
    return np.sum(result_grid)

def findNumMas(grid, index):
    row, col = index
    letters = np.array([
        [grid[row-1, col-1], #up left
        grid[row-1, col+1]], #up right
        [grid[row+1, col-1], #down left
        grid[row+1, col+1]] # down right
    ])
    if (''.join(letters[0, :]) == "MM" and ''.join(letters[1, :]) == "SS") or \
        (''.join(letters[1, :]) == "MM" and ''.join(letters[0, :]) == "SS") or \
        (''.join(letters[:, 0]) == "MM" and ''.join(letters[:, 1]) == "SS") or \
        (''.join(letters[:, 1]) == "MM" and ''.join(letters[:, 0]) == "SS"):
        return 1
    return 0