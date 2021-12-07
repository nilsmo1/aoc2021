# Day 7, Treachery of Whales

from typing import List

# Q1
def min_fuel(crabs: List[int]) -> int:
    cost = min(sum(abs(c - c1) for c in crabs) for c1 in crabs)
    return cost

# Q2
def min_fuel_arithmetic_sum(crabs: List[int]) -> int:
    n = lambda c, i: int(abs(c - i) * (abs(c - i) + 1) / 2)
    cost = min(sum(n(c, i) for c in crabs) for i in range(max(crabs)))
    return cost

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [int(x) for x in sample.read().strip().split(',')]

    # Tests
    assert min_fuel(sample_input) == 37

    assert min_fuel_arithmetic_sum(sample_input) == 168

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [int(x) for x in RAW.read().strip().split(',')]
    
    # Results
    print(f'Q1: {min_fuel(formatted)}')
    print(f'Q2: {min_fuel_arithmetic_sum(formatted)}')
