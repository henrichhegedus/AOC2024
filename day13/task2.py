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


def almost_int(x):
    return abs(x - np.floor(x)) < 10**-4 or abs(x - np.ceil(x)) < 10**-4
        

def get_lowest_cost(machine):
    end_x, end_y = machine["p"]["x"], machine["p"]["y"]
    dax, day = machine["a"]["x"], machine["a"]["y"]
    dbx, dby = machine["b"]["x"], machine["b"]["y"]

    a = np.array([[dax, dbx], [day, dby]])
    b = np.array([end_x, end_y])

    a, b = np.linalg.solve(a,b)

    print("a", a)
    print("b", b)
    
    if almost_int(a) and almost_int(b):
        return a*3 +b
    
    return 0



def get_machines(matrix):
    machines = []
    for i in range(0, len(matrix),4):
        a = get_vals(matrix[i])
        b = get_vals(matrix[i+1])
        prize = get_vals(matrix[i+2])
        prize['x'] += 10000000000000
        prize['y'] += 10000000000000

        machines.append({"a": a, "b": b, "p": prize})

    return machines


def day_code(matrix):
    machines = get_machines(matrix)
    total = 0
    for i, machine in tqdm(enumerate(machines), total=len(machines)):
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
