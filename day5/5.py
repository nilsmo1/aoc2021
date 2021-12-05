# Day 5, Hydrothermal Venture

from collections import defaultdict
from typing import NamedTuple, List, Tuple

class PointPair(NamedTuple):
    x1 : int
    x2 : int
    y1 : int
    y2 : int
    
    @property
    def valid(self) -> bool:
        return (self.x1 == self.x2 or 
                self.y1 == self.y2)
    
    def points(self) -> List[Tuple[int, int]]:
        assert self.valid
        if self.x1 != self.x2:
            x_low, x_high = min(self.x1, self.x2), max(self.x1, self.x2)
            points = [(x, self.y1) for x in range(x_low, x_high+1)]
            return points    
        y_low, y_high = min(self.y1, self.y2), max(self.y1, self.y2)
        points = [(self.x1, y) for y in range(y_low, y_high+1)]
        return points    

    def diagonal_points(self) -> List[Tuple[int, int]]:
        assert not self.valid
        slope = 1 if (self.y2 - self.y1)/(self.x2 - self.x1) > 0 else -1
        x_low, x_high = min(self.x1, self.x2), max(self.x1, self.x2)
        y_low, y_high = min(self.y1, self.y2), max(self.y1, self.y2)
        y = y_low if slope > 0 else y_high
        points = [(x_low + x, x * slope + y) for x in range(abs(self.x2 - self.x1)+1)]
        return points

    @classmethod
    def from_string(cls, line: str) -> 'PointPair':
        pair1, pair2 = line.split(' -> ')
        x1, y1 = pair1.split(',')
        x2, y2 = pair2.split(',')
        return cls(int(x1), int(x2),
                   int(y1), int(y2))

# Q1
def get_overlaps(pairs: List[PointPair]) -> int:
    valid_point_count = defaultdict(int)
    valid_pairs = [pair for pair in pairs if pair.valid]
    for pair in valid_pairs:
        for point in pair.points():
            valid_point_count[point] += 1
    return sum(1 for e in valid_point_count.values() if e > 1)

# Q2
def get_overlaps_with_diagonals(pairs: List[PointPair]) -> int:
    valid_point_count = defaultdict(int)
    for pair in pairs:
        for point in pair.points() if pair.valid else pair.diagonal_points():
            valid_point_count[point] += 1
    return sum(1 for e in valid_point_count.values() if e > 1)

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [PointPair.from_string(line.strip()) 
                        for line in sample.readlines()]
    
    # Tests
    assert get_overlaps(sample_input) == 5
    assert get_overlaps_with_diagonals(sample_input) == 12

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [PointPair.from_string(line.strip()) 
                     for line in RAW.readlines()] 

    # Results
    print(f'Q1: {get_overlaps(formatted)}')
    print(f'Q2: {get_overlaps_with_diagonals(formatted)}')
