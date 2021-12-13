# Day 12, Passage Pathing

from typing import List, Dict, Optional
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
def find_paths_2(cave: str, end: str, current_path: List[str], caves: CaveDict, seen: bool=False) -> int:
    total = 0
    ends = ['start', 'end']
    if cave == end:
        total += 1
        #print(''.join(current_path))
        return total
    for neighbour in caves[cave]:
        if neighbour.islower():
            if neighbour in current_path and not seen and neighbour not in ends:
                current_path.append(cave)
                total += find_paths_2(neighbour, end, current_path, caves, True)
                current_path.pop()
            elif neighbour not in current_path and seen:
                current_path.append(cave)
                total += find_paths_2(neighbour, end, current_path, caves, True)
                current_path.pop()
            elif neighbour not in current_path and not seen:
                current_path.append(cave)
                total += find_paths_2(neighbour, end, current_path, caves)
                current_path.pop()
        if neighbour.isupper():
            if seen:
                current_path.append(cave)
                total += find_paths_2(neighbour, end, current_path, caves, True)
                current_path.pop()
            else:
                current_path.append(cave)
                total += find_paths_2(neighbour, end, current_path, caves)
                current_path.pop()
                
    return total

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [line.strip().split('-') for line in sample.readlines()]
        sample_caves = make_cave_dict(sample_input)

    # Tests
    assert paths(sample_caves) == 10

    assert find_paths_2('start', 'end', [], sample_caves) == 36

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [line.strip().split('-') for line in RAW.readlines()] 
        formatted_caves = make_cave_dict(formatted)

    # Results
    print(f'Q1: {paths(formatted_caves)}')
    print(f'Q2: {find_paths_2("start", "end", [], formatted_caves)}')
