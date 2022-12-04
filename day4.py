import os

day = 4
input_file = os.path.expanduser('~/Documents/Coding Projects/advent-of-code-2022/input/day'+str(day)+'.txt')

def read_input():
    with open(input_file,'r') as f:
        return f.read()

input = read_input()

def part1():
    inputs = input.split()
    sum = 0
    for line in inputs:
        a = line.replace('-',',').split(',')
        a = [int(x) for x in a]

        if (a[0]<=a[2] and a[1]>=a[3]) or (a[2]<=a[0] and a[3]>=a[1]):
            sum+=1

    return sum

def part2():
    inputs = input.split()
    sum = 0
    for line in inputs:
        a = line.replace('-',',').split(',')
        a = [int(x) for x in a]

        if (a[0]<=a[2] and a[2]<=a[1]) or (a[2]<=a[0] and a[0]<=a[3]):
            sum+=1

    return sum

def main():
    print(part1())
    print(part2())

main()