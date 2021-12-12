# Day 12, Passage Pathing

from typing import List, Dict, Set
CaveDict = Dict[str, List[str]]

def make_cave_dict(raw: List[List[str]]) -> CaveDict:
    caves = {}
    for c1, c2 in raw:
        if c1 not in caves: caves[c1] = []
        if c2 not in caves: caves[c2] = []
        caves[c1].append(c2)
        caves[c2].append(c1)
    return caves

# Q1
def find_paths(cave: str, end: str, current_path: List[str], caves: CaveDict) -> int:
    total = 0
    if cave == end:
        total += 1
        return total
    for neighbour in caves[cave]:
        if (neighbour.islower() and neighbour not in current_path) or neighbour.isupper():
            current_path.append(cave)
            total += find_paths(neighbour, end, current_path, caves)
            current_path.pop()
    return total

def paths(caves: CaveDict) -> int:
    return find_paths('start', 'end', [], caves)

# Q2
# TODO

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [line.strip().split('-') for line in sample.readlines()]
        sample_caves = make_cave_dict(sample_input)

    # Tests
    assert paths(sample_caves) == 226

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [line.strip().split('-') for line in RAW.readlines()] 
        formatted_caves = make_cave_dict(formatted)

    # Results
    print(f'Q1: {paths(formatted_caves)}')
    print(f'Q2: -')
