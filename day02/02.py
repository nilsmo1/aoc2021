# Day 2, Dive!

from typing import List, NamedTuple

class Instruction(NamedTuple):
    command  : str
    argument : int

def make_instruction(raw: str) -> Instruction:
    command, argument = raw.strip().split()
    return Instruction(command, int(argument))

# Q1
def parse(instructions: List[Instruction]) -> int:
    pos_x, pos_y = 0, 0
    for inst in instructions:
        if   inst.command == "forward": pos_x += inst.argument
        elif inst.command == "down"   : pos_y += inst.argument
        elif inst.command == "up"     : pos_y -= inst.argument
    return pos_x * pos_y

# Q2
def parse2(instructions: List[Instruction]) -> int:
    pos_x, pos_y, aim = 0, 0, 0
    for inst in instructions:
        if inst.command == "forward": 
            pos_x += inst.argument
            pos_y += aim * inst.argument
        elif inst.command == "down": 
            aim += inst.argument
        elif inst.command == "up": 
            aim -= inst.argument
    return pos_x * pos_y

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [make_instruction(line) for line in sample]
    
    # Tests
    assert parse(sample_input) == 150

    assert parse2(sample_input) == 900

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [make_instruction(line) for line in RAW] 
    
    # Results
    print(f'Q1: {parse(formatted)}')
    print(f'Q2: {parse2(formatted)}')
