# Day 1, Sonar Sweep
from typing import List

# Q1
def count_increasing(levels: List[int]) -> int:
    total = 0
    for i in range(1, len(levels)):
        if levels[i] > levels[i-1]: 
            total += 1
    return total

# Q2
def three_measurement_window(levels: List[int], index: int) -> int:
    return sum(levels[i] for i in (index, index+1, index+2))

def count_increasing_threes(levels: List[int]) -> int:
    total = 0
    for i in range(len(levels)-3):
        if three_measurement_window(levels, i) < three_measurement_window(levels, i+1):
            total += 1
    return total

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [int(line.strip()) for line in sample]
    assert(count_increasing(sample_input) == 7)
    assert(count_increasing_threes(sample_input) == 5)

    with open('puzzle-input', 'r') as RAW:
        formatted = [int(line.strip()) for line in RAW]
    # Q1
    print(f'Q1: {count_increasing(formatted)}')
    # Q2
    print(f'Q2: {count_increasing_threes(formatted)}')
