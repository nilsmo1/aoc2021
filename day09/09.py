# Day 9, Smoke Basin

from typing import List, Tuple

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
def neighbouring_coordinates(height_map: List[List[int]], row: int, col: int) -> List[Tuple[int, int]]:
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    neighbours = [(row+j, col+i)
                   for j,i in zip(dy, dx) 
                   if 0 <= row + j < len(height_map) and
                      0 <= col + i < len(height_map[0])]
    return neighbours
    
def flood_fill(height_map: List[List[int]], row: int, col: int) -> int:
    size = 0
    visited, not_visited = [], [(row, col)]
    while not_visited:
        r, c = not_visited.pop()
        visited.append((r, c))
        size += 1        
        for neighbour in neighbouring_coordinates(height_map, r, c):
            neighbour_r, neighbour_c = neighbour
            if not (neighbour in visited or
                    height_map[neighbour_r][neighbour_c] == 9 or
                    neighbour in not_visited):
                not_visited.append(neighbour)
    return size

def largest_basin_product(height_map: List[List[int]]) -> int:
    low_points = [(row, col)
                  for col in range(len(height_map[0]))
                  for row in range(len(height_map))
                  if less_than_neighbours(height_map, row, col)]
    
    basins = sorted([flood_fill(height_map, row, col) 
                     for row, col in low_points])
      
    return basins[-1] * basins[-2] * basins[-3]

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [list(line.strip()) for line in sample]
        sample_ints = [[int(x) for x in line] for line in sample_input]

    # Tests
    assert sum_risk_levels(sample_ints) == 15

    assert largest_basin_product(sample_ints) == 1134

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [list(line.strip()) for line in RAW] 
        formatted_ints = [[int(x) for x in line] for line in formatted]

    # Results
    print(f'Q1: {sum_risk_levels(formatted_ints)}')
    print(f'Q2: {largest_basin_product(formatted_ints)}')
