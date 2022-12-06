import os

day = 6
input_file = os.path.expanduser('~/Documents/Coding Projects/advent-of-code-2022/input/day'+str(day)+'.txt')

def read_input():
    with open(input_file,'r') as f:
        return f.read()

input = read_input()

def part1():
    for i in range(4,len(input)):
        if len(set(input[i-4:i])) == 4:
            return i

def part2():
    for i in range(14,len(input)):
        if len(set(input[i-14:i])) == 14:
            return i

def main():
    print(part1())
    print(part2())

main()