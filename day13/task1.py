import argparse
import pathlib
import numpy as np
from operator import *
from heapq import heappush, heappop, heapify
from tqdm import tqdm


dir = pathlib.Path(__file__).parent.resolve()

parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')


def in_matrix(i, j, matrix):
    return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])

def get_vals(line):
    x, y = line.split(" ")[-2:]

    x = int(x[2:-1])
    y = int(y[2:])

    return {"x":x, "y":y}
        

def get_lowest_cost(machine):
    end_x, end_y = machine["p"]["x"], machine["p"]["y"]

    # f, g, h, x, y
    start = [end_x**2 + end_y**2, 0, end_x**2 + end_y**2, 0, 0]
    

    open_minheap = [start]
    visited = set()

    while open_minheap:
        node = heappop(open_minheap)
        visited.add((node[-2], node[-1]))
        if node[3] == end_x and node[4] == end_y:
            return node[1]

        for button in ["a", "b"]:
            movements = machine[button]
            cost = 3 if button == "a" else 1

            next_node = [0, node[1] + cost, 0, node[3] + movements["x"], node[4] + movements["y"]]
            next_node[2] = (end_x - next_node[3])**2 + (end_y - next_node[4])**2
            next_node[0] = next_node[1] + next_node[2]

            if (next_node[-2], next_node[-1]) in visited or next_node[-2] > end_x or next_node[-1] > end_y:
                continue
            else:
                heappush(open_minheap, next_node)

    return 0



def get_machines(matrix):
    machines = []
    for i in tqdm(range(0, len(matrix),4), total= len(matrix)):
        a = get_vals(matrix[i])
        b = get_vals(matrix[i+1])
        prize = get_vals(matrix[i+2])

        machines.append({"a": a, "b": b, "p": prize})

    return machines


def day_code(matrix):
    machines = get_machines(matrix)
    total = 0
    for machine in machines:
        total += get_lowest_cost(machine)

    return total


def main():
    args = parser.parse_args()
    if args.test:
        print("test input")
        filename = f'{dir}/test_input.txt'
    else:
        filename = f'{dir}/input.txt'

    file = open(filename, 'r')
    lines = [l.strip() for l in file.readlines()]

    print(day_code(lines))


if __name__ == '__main__':
    main()
