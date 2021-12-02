# Day 1, Sonar Sweep

from typing import List

# Q1
def count_increasing(levels: List[int]) -> int:
    return sum(1 for i in range(len(levels)-1) if levels[i] < levels[i+1])

# Q2
def three(levels: List[int], index: int) -> int:
    return sum(e for e in levels[index:index+3])

def count_increasing_threes(levels: List[int]) -> int:
    return sum(1 for i in range(len(levels)-3) if three(levels, i) < three(levels, i+1))

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [int(line.strip()) for line in sample]
    
    # Tests
    assert count_increasing(sample_input) == 7
    assert count_increasing_threes(sample_input) == 5
    
    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [int(line.strip()) for line in RAW]
    
    # Results    
    print(f'Q1: {count_increasing(formatted)}')
    print(f'Q2: {count_increasing_threes(formatted)}')
