# Day 10, Syntax Scoring

from typing import List, Optional

# Q1
def get_corrupted_char(chunk: str) -> Optional[str]:
    relatives = {'(' : ')', '{' : '}', '[' : ']', '<' : '>'}
    order = []
    for c in chunk:
        if c in relatives.values():
            if relatives[order[-1]] != c: return c
            else: order = order[:-1]
        else: order.append(c)
    return None

def get_points(chunks: List[str]) -> int:
    points = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
    chars = [get_corrupted_char(chunk) for chunk in chunks]
    chars_not_none = [char for char in chars if char is not None]
    return sum(points[char] for char in chars_not_none)

# Q2
def get_chunk_completion(chunk: str) -> Optional[str]:
    relatives = {'(' : ')', '{' : '}', '[' : ']', '<' : '>'}
    order = []
    for c in chunk:
        if c in relatives.values():
            if relatives[order[-1]] != c: return None
            else: order = order[:-1]
        else: order.append(c)
    complete = []
    for c in order[::-1]:
        complete.append(relatives[c])
        order = order[:-1]
    return ''.join(complete)

def score_chunk(chunk: str) -> int:
    points = {')' : 1, ']' : 2, '}' : 3, '>' : 4}
    total = 0
    for c in chunk:
        total = 5*total + points[c]
    return total

def completed_chunk_scores(chunks: str) -> int:
    completions = [get_chunk_completion(chunk) for chunk in chunks]
    completions = [completion for completion in completions if completion is not None]
    points = [score_chunk(completion) for completion in completions]
    middle_index = int(len(points)/2)
    return sorted(points)[middle_index]

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [line.strip() for line in sample.readlines()]

    # Tests
    assert get_points(sample_input) == 26397
    
    assert completed_chunk_scores(sample_input) == 288957

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [line.strip() for line in RAW.readlines()] 
    
    # Results
    print(f'Q1: {get_points(formatted)}')
    print(f'Q2: {completed_chunk_scores(formatted)}')
