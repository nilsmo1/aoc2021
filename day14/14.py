# Day 14, Extended Polymerization

from collections import Counter
from typing import List, Dict, Tuple
Polymer = str
Instruction = Tuple[str, str]

def make_instruction_dict(raw: List[str]) -> Dict[Instruction, str]:
    instructions = {}
    for fr, insertion in raw:
        fr, to = fr
        instructions[(fr,to)] = insertion
    return instructions

# Q1
def get_polymer(instructions: Dict[Instruction, str], template: Polymer, rounds: int) -> Polymer:
    for step in range(rounds):
        new_polymer = []
        for i, c in enumerate(list(template[:-1])):
            key = c, template[i+1]
            new_polymer.append(c)
            new_polymer.append(instructions[key])
        new_polymer.append(template[-1])
        template = ''.join(new_polymer)
    return template


def differance_least_most_common(polymer: Polymer) -> int:
    counts = Counter(polymer)
    return max(counts.values()) - min(counts.values())

# Q2

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [line.strip().split('\n') for line in sample.read().split('\n\n')]
        sample_instructions = make_instruction_dict([line.split(' -> ') for line in sample_input[-1]])
        sample_template = sample_input[0][0]

    # Tests
    sample_polymer1 = get_polymer(sample_instructions, sample_template, 10)
    assert differance_least_most_common(sample_polymer1) == 1588
    
    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted_input = [line.strip().split('\n') for line in RAW.read().split('\n\n')]
        formatted_instructions = make_instruction_dict([line.split(' -> ') for line in formatted_input[-1]])
        formatted_template = formatted_input[0][0]
    polymer1 = get_polymer(formatted_instructions, formatted_template, 10)

    # Results
    print(f'Q1: {differance_least_most_common(polymer1)}')
    print(f'Q2: --')
