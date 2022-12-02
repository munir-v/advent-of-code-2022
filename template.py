import os

input_file = os.path.expanduser('~/Documents/Coding Projects/advent-of-code-2022/input/day')

def read_input():
    with open(input_file,'r') as f:
        return f.readlines()