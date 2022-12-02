import os

day = 1
input_file = os.path.expanduser('~/Documents/Coding Projects/advent-of-code-2022/input/day'+str(day)+'.txt')

def read_input():
    with open(input_file,'r') as f:
        return f.read()

input = read_input()

def part1():
    calories_groups = input.split('\n\n')
    calories = []
    for group in calories_groups:
        nums = [int(n) for n in group.split('\n')]
        calories.append(sum(nums))

    return max(calories)

def part2():
    calories_groups = input.split('\n\n')
    calories = []
    calorie_sum = 0
    for group in calories_groups:
        nums = [int(n) for n in group.split('\n')]
        calories.append(sum(nums))

    for i in range(3):
        cur_max = max(calories)
        calorie_sum += cur_max
        calories.remove(cur_max)

    return calorie_sum

def main():
    print(part1())
    print(part2())

main()