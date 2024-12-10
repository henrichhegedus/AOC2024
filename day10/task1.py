import argparse
import pathlib
import numpy as np
from operator import *

dir = pathlib.Path(__file__).parent.resolve()

parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')


def in_matrix(i, j, matrix):
    return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])


def get_trailheads(matrix):
    trailheads = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                trailheads.append((i,j))


    return trailheads



def day_code(matrix):
    trailheads = get_trailheads(matrix)
    scores = []
    print(trailheads)
    for trailhead in trailheads:
        queue = [trailhead]
        trailends = set()

        while queue:
            pos = queue.pop()
            i, j = pos

            val = matrix[i][j]

            if val == 9:
                trailends.add(pos)
                continue

            for (i_i, j_j) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if in_matrix(i_i,j_j, matrix) and matrix[i_i][j_j] == val + 1:
                    queue.append((i_i,j_j))


        scores.append(len(trailends))

    return sum(scores)
                

def main():
    args = parser.parse_args()
    if args.test:
        print("test input")
        filename = f'{dir}/test_input.txt'
    else:
        filename = f'{dir}/input.txt'

    file = open(filename, 'r')
    lines = [[int(x) if x.isnumeric() else -1 for x in l.strip() ] for l in file.readlines()]

    print(day_code(lines))


if __name__ == '__main__':
    main()
