import os

day = 3
input_file = os.path.expanduser('~/Documents/Coding Projects/advent-of-code-2022/input/day'+str(day)+'.txt')

def read_input():
    with open(input_file,'r') as f:
        return f.read()

input = read_input()

def part1():
    data = input.split()
    sum = 0
    for line in data:
        half = int(len(line) / 2)
        unique_char = set(line[:half]) & set(line[half:])
        cur = ord(list(unique_char)[0])
        if cur >= 97:
            sum += cur - 96
        else:
            sum += cur - 64 + 26
    return sum

def part2():
    data = input.split()
    sum = 0
    i = 0
    while i < len(data):
        unique_char = set(data[i]) & set(data[i+1]) & set(data[i+2])
        cur = ord(list(unique_char)[0])
        if cur >= 97:
            sum += cur - 96
        else:
            sum += cur - 64 + 26
        i+=3
    return sum

def main():
    print(part1())
    print(part2())

main()