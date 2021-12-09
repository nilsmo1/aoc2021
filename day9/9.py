# Day 9, Smoke Basin

from typing import List

# Q1
def less_than_neighbours(height_map: List[List[int]], row: int, col: int) -> bool:
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    info = [height_map[row][col] < height_map[row + j][col + i] 
            for j,i in zip(dy, dx) 
            if 0 <= row + j < len(height_map) and
               0 <= col + i < len(height_map[0])]
    return all(info)

def sum_risk_levels(height_map: List[List[int]]) -> int:
    risk_levels = [d + 1 
                   for row, ds in enumerate(height_map)
                   for col, d in enumerate(ds) 
                   if less_than_neighbours(height_map, row, col)]
    return sum(risk_levels) 

# Q2
def neighbouring_9s(height_map: List[List[int]], row: int, col: int) -> bool:
    dx = dy = [-1, 0, 1]
    info = [(row+j, col+i) 
            for i in dx
            for j in dy
            if 0 <= row + j < len(height_map)    and
               0 <= col + i < len(height_map[0]) and
               height_map[row+j][col+i] == 9]
    return info

def get_basin_sizes(height_map: List[List[int]]) -> List[int]:
    low_points = [(row, col)
                  for col in range(len(height_map[0]))
                  for row in range(len(height_map))
                  if less_than_neighbours(height_map, row, col)]
    #TODO

def three_largest_basins_product(height_map: List[List[int]]) -> int:
    basin_sizes = get_basin_sizes(height_map)
    #TODO

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [list(line.strip()) for line in sample]
        sample_ints = [[int(x) for x in line] for line in sample_input]
    get_basin_sizes(sample_ints)

    # Tests
    assert sum_risk_levels(sample_ints) == 15

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [list(line.strip()) for line in RAW] 
        formatted_ints = [[int(x) for x in line] for line in formatted]

    # Results
    print(f'Q1: {sum_risk_levels(formatted_ints)}')
    print(f'Q2: ')
