import os
import re
from pprint import pprint

day = 5
input_file = os.path.expanduser('~/Documents/Coding Projects/advent-of-code-2022/input/day'+str(day)+'.txt')

def read_input():
    with open(input_file,'r') as f:
        return f.read()

input = read_input().split('\n')

def get_boxes(input):
    box_input = input[:8]
    boxes = [[] for i in range(9)] # list of 9 empty lists
    for box in box_input:
        j = 0
        while j<9*4:
            cur_char = box[j+1]
            if not cur_char == ' ':
                boxes[j//4].append(cur_char)
            j+=4
    return boxes

def get_moves(input):
    instructions = input[10:]
    moves = []
    for line in instructions:
        cur_move = re.findall(r'\d+',line)
        moves.append(cur_move)
    return moves

def perform_moves1(boxes,moves):
    for move in moves:
        num_to_move = int(move[0])
        move_from = int(move[1])-1
        move_to = int(move[2])-1

        for i in range(num_to_move):
            cur_box = boxes[move_from].pop(0)
            boxes[move_to].insert(0,cur_box)
    return boxes

def get_top_boxes(new_boxes):
    retval = ''
    for i in range(9):
        retval+=new_boxes[i][0]
    return retval

def part1():
    boxes = get_boxes(input)
    moves = get_moves(input)
    new_boxes = perform_moves1(boxes,moves)
    top_boxes = get_top_boxes(new_boxes)

    return top_boxes

def perform_moves2(boxes,moves):
    for move in moves:
        num_to_move = int(move[0])
        move_from = int(move[1])-1
        move_to = int(move[2])-1

        cur_box = boxes[move_from][:num_to_move]
        del boxes[move_from][:num_to_move]
        boxes[move_to] = cur_box + boxes[move_to]
    return boxes

def part2():
    boxes = get_boxes(input)
    moves = get_moves(input)
    new_boxes = perform_moves2(boxes,moves)
    top_boxes = get_top_boxes(new_boxes)

    return top_boxes

def main():
    print(part1())
    print(part2())

main()