# Day 8, Seven Segment Search

from typing import List, Tuple
In_Out = Tuple[List[str], List[str]]

# Q1
def count_uniques(words: List[In_Out]) -> int:
    total = 0
    for _, out in words:
        out = [len(x) for x in out]
        total += sum(out.count(x) for x in [2, 4, 3, 7])
    return total

# Q2

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [line.strip().split(' | ') for line in sample.readlines()]
        sample_words = [(line[0].split(), line[1].split()) for line in sample_input]

    # Tests
    assert count_uniques(sample_words) == 26

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [line.strip().split(' | ') for line in RAW.readlines()]
        formatted_words = [(line[0].split(), line[1].split()) for line in formatted]
    
    # Results
    print(f'Q1: {count_uniques(formatted_words)}')
    print(f'Q2: ')
