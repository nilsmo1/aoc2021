# Day 4, Giant Squid

from typing import List

class BingoBoard:
    def __init__(self, layout: List[List[int]]) -> None:
        self.layout = layout
        self.shown = []
    
    def add_to_shown(self, num: int) -> None:
        self.shown.append(num)
    
    @property
    def winner(self) -> bool:
        pass

    @property
    def final_score(self) -> int:
        return sum(x for x in line for line in self.layout if x not in self.shown)

#def make_BingoBoard(layout: 

# Q1


# Q2

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input   = sample.read().split('\n')
    sample_numbers = sample_input[0]
    sample_boards  = [line for line in sample_input[1:] if line]
    
    # Tests
    
    # Puzzle input
    #with open('puzzle-input', 'r') as RAW:
    #    formatted = [int(line.strip()) for line in RAW] 
    
    # Results
    print(f'Q1: ')
    print(f'Q2: ')
