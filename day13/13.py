# Day 13, Transparent Origami

from typing import List, Tuple
Fold = Tuple[str, int]
Point = List[int]

def make_points(points: List[List[str]]) -> List[Point]:
    return [[int(x), int(y)] for x,y in points]

def make_folds(folds: List[List[str]]) -> List[Tuple]:
    return [(x, int(val)) for x, val in folds]

# Q1
def get_remaining_points(points: List[Point], fold: Fold) -> int:
    axis, val = fold
    if   axis == 'y': points = list(filter(lambda x: x[1] != val, points))
    elif axis == 'x': points = list(filter(lambda x: x[0] != val, points))
    for point in points:
        x, y = point
        if   axis == 'y' and y > val: point[1] = 2*val - y
        elif axis == 'x' and x > val: point[0] = 2*val - x
        new_points = []
        for point in points:
            if point not in new_points: new_points.append(point)
        points = new_points
    return len(points)

# Q2
def get_remaining_points_all_folds(points: List[Point], folds: List[Fold]) -> None:
    for axis, val in folds:
    #print(axis, val)
    #print(sorted(points, key=lambda x: x[0]))
        if   axis == 'y': points = list(filter(lambda x: x[1] != val, points))
        elif axis == 'x': points = list(filter(lambda x: x[0] != val, points))
        for point in points:
            x, y = point
            if   axis == 'y' and y > val: point[1] = 2*val - y
            elif axis == 'x' and x > val: point[0] = 2*val - x
            new_points = []
            for point in points:
                if point not in new_points: new_points.append(point)
            points = new_points
    #print(sorted(points, key=lambda x: x[0]))
    xmax = max(points, key=lambda x: x[0])[0]
    ymax = max(points, key=lambda x: x[1])[1]
    grid = [['#' if [x,y] in points else ' ' for x in range(xmax+1)] for y in range(ymax+1)]
    for line in grid:
        print(' '.join(line))

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_points, sample_folds = sample.read().split('\n\n')
        sample_points = [point.strip().split(',') for point in sample_points.split('\n')]
        sample_folds = [fold.strip().split()[2].split('=') for fold in sample_folds.split('\n') if fold]
    sample_points = make_points(sample_points)
    sample_folds = make_folds(sample_folds)

    # Tests
    assert get_remaining_points(sample_points, sample_folds[0]) == 17
    
    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted_points, formatted_folds = RAW.read().split('\n\n')
        formatted_points = [point.strip().split(',') for point in formatted_points.split('\n')]
        formatted_folds = [fold.strip().split()[2].split('=') for fold in formatted_folds.split('\n') if fold]
    points = make_points(formatted_points)
    folds = make_folds(formatted_folds)

    # Results
    print(f'Q1: {get_remaining_points(points, folds[0])}')
    print('Q2: ')
    get_remaining_points_all_folds(points, folds)
