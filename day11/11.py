# Day 11, Dumbo Octopus

from typing import List, Tuple

# Q1
def tens_present(grid: List[List[int]]) -> bool:
    return any(x == 10 for row in grid for x in row)

def reset_grid(grid: List[List[int]]) -> List[List[int]]:
    return [[x if x!=-1 else 0 for x in row] for row in grid]

def neighbour_coordinates(rows: int, cols: int, row: int, col: int) -> List[Tuple[int, int]]:
    return [(row+i, col+j)
             for i in [-1, 0, 1]
             for j in [-1, 0, 1]
             if 0 <= row+i < rows and
                0 <= col+j < cols and 
                not i == j == 0]
    
def flash(grid: List[List[int]], row: int, col: int) -> Tuple[int, List[List[int]]]:
    total_flashes = 1
    grid[row][col] = -1
    rows = len(grid)
    cols = len(grid[0])
    neighbours = neighbour_coordinates(rows, cols, row, col)
    for r, c in neighbours:
        if grid[r][c] != -1:
            grid[r][c] += 1
        if grid[r][c] >= 10:
            flashes, grid = flash(grid, r, c)
            total_flashes += flashes
    return total_flashes, grid

def step(grid: List[List[int]], steps: int) -> int:
    total_flashes = 0
    for step in range(steps):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += 1
        while tens_present(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 10:
                        flashes, grid = flash(grid, i, j)
                        total_flashes += flashes
        grid = reset_grid(grid)
    return total_flashes

# Q2
def all_zeros(grid: List[List[int]]) -> bool:
    return all(x == 0 for row in grid for x in row)
    
def get_all_flashing(grid: List[List[int]]) -> int:
    count_days = 1
    while True:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += 1
        while tens_present(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 10:
                        _, grid = flash(grid, i, j)
        grid = reset_grid(grid)
        count_days += 1
        if all_zeros(grid):
            return count_days

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [list(line.strip()) for line in sample.readlines()]
        sample_ints = [[int(x) for x in row] for row in sample_input]
    
    # Tests
    assert step(sample_ints, 100) == 1656
    
    assert get_all_flashing(sample_ints) == 195

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [list(line.strip()) for line in RAW.readlines()] 
        formatted_ints = [[int(x) for x in row] for row in formatted]
    
    # Results
    print(f'Q1: {step(formatted_ints, 100)}')
    print(f'Q2: {get_all_flashing(formatted_ints)}')
