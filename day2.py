import os

day = 2
input_file = os.path.expanduser('~/Documents/Coding Projects/advent-of-code-2022/input/day'+str(day)+'.txt')

def read_input():
    with open(input_file,'r') as f:
        return f.read()

input = read_input()

def part1():
    rounds = []
    for x in input.split('\n'):
        rounds.append(x.split(' '))

    total_score = 0

    for round in rounds:
        them = round[0]
        us = round[1]
        them = "ABC".index(them)
        us = "XYZ".index(us)

        total_score += us + 1

        if (them - us) % 3 == 0: # draw
            total_score += 3
        elif (them - us) % 3 == 2: # win
            total_score += 6

    return total_score

def part2():
    

    return total_score

def main():
    print(part1())
    print(part2())

main()