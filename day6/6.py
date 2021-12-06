# Day 6, Lanternfish

from typing import List, Dict

# Q1
def model_fish_growth(initial_state: List[int], number_of_days: int) -> int:
    growth_model = initial_state
    for _ in range(number_of_days):
        growth_model = list(map(lambda x: x-1 if x != 0 else 6, growth_model))
        growth_model += [9 for _ in range(growth_model.count(0))]
    return len(growth_model) - growth_model.count(9)

# Q2
def dict_from_initial_state(initial_state: List[int]) -> Dict[int, int]:
    return {x : initial_state.count(x) for x in range(9)}

def dict_growth_model(initial_state: List[int], number_of_days: int) -> int:
    state_dict = dict_from_initial_state(initial_state)
    prev_zeros = 0
    for day in range(number_of_days):
        for num in state_dict:
            if num != 8:
                state_dict[num] = state_dict[num+1]
        state_dict[6] += prev_zeros
        state_dict[8] = prev_zeros
        prev_zeros = state_dict[0]
    return sum(x for x in state_dict.values())

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [int(x) for x in sample.read().strip().split(',')]
    
    # Tests
    assert model_fish_growth(sample_input,  80) == 5934
    
    assert dict_growth_model(sample_input, 256) == 26984457539
    
    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [int(x) for x in RAW.read().strip().split(',')] 
    
    # Results
    print(f'Q1: {model_fish_growth(formatted,  80)}')
    print(f'Q2: {dict_growth_model(formatted, 256)}')
