# Day 3, Binary Diagnostic

from typing import List

# Q1
def epsilon_gamma_product(nums: List[str]) -> int:
    cols = [[nums[row][col] 
             for row in range(len(nums))] 
             for col in range(len(nums[0]))]
    max_counts = [max(col, key=col.count) for col in cols]  
    epsilon = int(''.join(max_counts), 2)
    gamma   = int(''.join(list(map(lambda x: '1' if x == '0' else '0', max_counts))), 2)
    return epsilon * gamma

# Q2
def oxygen(nums: List[str]) -> int:
    pos = 0
    col_size = len(nums[0])
    while pos < col_size:
        col = [nums[row][pos] for row in range(len(nums))]
        max_count = '1' if col.count('1') >= col.count('0') else '0'
        nums = list(filter(lambda x: x[pos] == max_count, nums))
        pos += 1
        if len(nums) == 1:
            return int(nums[0], 2)
            
def co2(nums: List[str]) -> int:
    pos = 0
    col_size = len(nums[0])
    while pos < col_size:
        col = [nums[row][pos] for row in range(len(nums))]
        max_count = '1' if col.count('1') < col.count('0') else '0'
        nums = list(filter(lambda x: x[pos] == max_count, nums))
        pos += 1
        if len(nums) == 1:
            return int(nums[0], 2)

if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [line.strip() for line in sample]
    
    # Tests
    assert epsilon_gamma_product(sample_input) == 198
    
    assert oxygen(sample_input) == 23 
    assert co2(sample_input)    == 10

    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [line.strip() for line in RAW] 
    
    # Results
    print(f'Q1: {epsilon_gamma_product(formatted)}')
    print(f'Q2: {oxygen(formatted) * co2(formatted)}')
