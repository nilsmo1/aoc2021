# Day 4, Giant Squid

from typing import List
Board = List[List[int]]

class BingoBoard:
    def __init__(self, layout: Board) -> None:
        self.layout = [row for row in layout if row]
        self.bingo_flag = False

    @property
    def get_bingo_flag(self) -> bool:
        return self.bingo_flag

    def set_bingo_flag(self) -> None:
        self.bingo_flag = True

    def winner(self, shown: List[int]) -> bool:
        cols  = [[row[i] for row in self.layout] for i in range(len(self.layout[0]))]
        rows  = self.layout
        for row, col in zip(cols, rows):
            if all(e in shown for e in row) or all(e in shown for e in col):
                return True

    def final_score(self, shown: List[int]) -> int:
        return shown[-1] * sum(sum(x for x in line if x not in shown) for line in self.layout)

def make_BingoBoards(layout: List[Board]) -> BingoBoard:
    return [BingoBoard(board) for board in layout]

# Q1
def run_bingo(numbers: List[int], boards: List[BingoBoard]) -> int:
    shown = numbers[:4]
    for number in numbers[4:]:
        shown.append(number)
        for board in boards:
            if board.winner(shown):
                return board.final_score(shown)
    raise ValueError('No winner!')

# Q2
def run_bingo_last_board(numbers: List[int], boards: List[BingoBoard]) -> int:
    num_winners_left = len(boards)
    shown = numbers[:4]
    for number in numbers[4:]:
        shown.append(number)
        for board in boards:
            if board.winner(shown) and not board.get_bingo_flag:
                num_winners_left -= 1
                board.set_bingo_flag()
                if not num_winners_left:
                    return board.final_score(shown)
    raise ValueError('No winner!')

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input   = sample.read().split('\n\n')
    sample_numbers = [int(e) for e in sample_input[0].split(',')]
    sample_boards  = [list(map(
                      lambda x: list(map(int, x.split())),
                      line.split('\n')))
                      for line in sample_input[1:] if line]
    sample_BingoBoards = make_BingoBoards(sample_boards)
    
    # Tests
    assert run_bingo(sample_numbers, sample_BingoBoards) == 4512
    
    assert run_bingo_last_board(sample_numbers, sample_BingoBoards) == 1924

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = RAW.read().split('\n\n')
    formatted_numbers = [int(e) for e in formatted[0].split(',')]
    formatted_boards  = [list(map(
                         lambda x: list(map(int, x.split())), 
                         line.split('\n'))) 
                         for line in formatted[1:] if line]
    formatted_BingoBoards = make_BingoBoards(formatted_boards)

    # Results
    print(f'Q1: {run_bingo(formatted_numbers, formatted_BingoBoards)}')
    print(f'Q2: {run_bingo_last_board(formatted_numbers, formatted_BingoBoards)}')
