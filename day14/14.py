# Day 14, Extended Polymerization

from collections import Counter, defaultdict
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
def get_polymer_smart(instructions: Dict[Instruction, str], template: Polymer, rounds: int) -> int:
    pairs = defaultdict(int)
    for i, c in enumerate(list(template[:-1])):
        pairs[c,template[i+1]] += 1
    for r in range(rounds):
        new_pairs = defaultdict(int)
        for pair in [pair for pair in pairs if pairs[pair]]:
            c1, c2 = tuple(pair)
            count = pairs[c1, c2]
            pairs[c1, c2] -= count
            new_pairs[c1, instructions[c1,c2]] += count
            new_pairs[instructions[c1,c2], c2] += count
        pairs = new_pairs
    chars = {c for t in pairs for c in t}
    counts = defaultdict(int)
    for c in chars:
        for pair, val in pairs.items():
            if c == pair[0]: counts[c] += val
    counts[template[-1]]+=1
    return max(counts.values()) - min(counts.values())

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [line.strip().split('\n') for line in sample.read().split('\n\n')]
        sample_instructions = make_instruction_dict([line.split(' -> ') for line in sample_input[-1]])
        sample_template = sample_input[0][0]

    # Tests
    sample_polymer1 = get_polymer(sample_instructions, sample_template, 10)
    assert differance_least_most_common(sample_polymer1) == 1588
   
    get_polymer_smart(sample_instructions, sample_template, 40) == 2188189693529

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted_input = [line.strip().split('\n') for line in RAW.read().split('\n\n')]
        formatted_instructions = make_instruction_dict([line.split(' -> ') for line in formatted_input[-1]])
        formatted_template = formatted_input[0][0]
    polymer1 = get_polymer(formatted_instructions, formatted_template, 10)
    polymer2 = get_polymer_smart(formatted_instructions, formatted_template, 40)

    # Results
    print(f'Q1: {differance_least_most_common(polymer1)}')
    print(f'Q2: {polymer2}')
