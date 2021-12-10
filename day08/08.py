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
def figure_stuff_out(word: In_Out) -> int:
    deduction = {}
    for s in word[0]:
        if   len(s) == 2: deduction[1] = s
        elif len(s) == 3: deduction[7] = s
        elif len(s) == 4: deduction[4] = s
        elif len(s) == 7: deduction[8] = s

    for s in word[0]:
        if len(s) == 5:
            if all([c in s for c in deduction[7]]):
                deduction[3] = s
            elif all([c in s for c in deduction[4] if c not in deduction[1]]):
                deduction[5] = s
            else: 
                deduction[2] = s

    for s in word[0]:
        if len(s) == 6:
            if not all([c in s for c in deduction[1]]):
                deduction[6] = s
            elif all([c in s for c in deduction[4] if c not in deduction[1]]):
                deduction[9] = s
            else:
                deduction[0] = s

    out = int(''.join([str(i) for x in word[1] for i in range(10) if sorted(x) == sorted(deduction[i])]))
    return out

def sum_results(rows: List[In_Out]) -> int:
    return sum(figure_stuff_out(row) for row in rows)

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [line.strip().split(' | ') for line in sample.readlines()]
        sample_words = [(line[0].split(), line[1].split()) for line in sample_input]

    # Tests
    assert count_uniques(sample_words) == 26

    assert sum_results(sample_words) == 61229

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [line.strip().split(' | ') for line in RAW.readlines()]
        formatted_words = [(line[0].split(), line[1].split()) for line in formatted]
    
    # Results
    print(f'Q1: {count_uniques(formatted_words)}')
    print(f'Q2: {sum_results(formatted_words)}')
