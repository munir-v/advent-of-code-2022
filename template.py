import os

day = 1
input_file = os.path.expanduser('~/Documents/Coding Projects/advent-of-code-2022/input/day'+str(day)+'.txt')

def read_input():
    with open(input_file,'r') as f:
        return f.read()

input = read_input()

def part1():
    pass

def part2():
    pass

def main():
    print(part1())
    # print(part2())

main()