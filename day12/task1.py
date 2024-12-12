import argparse
import pathlib
import numpy as np
from operator import *

dir = pathlib.Path(__file__).parent.resolve()

parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')


def in_matrix(i, j, matrix):
    return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])


def perimeter(patch, matrix):
    size = 0

    for i,j in patch:
        for n_i, n_j in [(i, j + 1), (i, j - 1), (i + 1, j), (i -1, j)]:
            if not (n_i, n_j) in patch or not in_matrix(n_i, n_j, matrix):
                size += 1

    return size





def day_code(matrix):
    marked = [[0] * len(matrix[0]) for _ in matrix]
    patches =  []

    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[i]):
            if marked[i][j]:
                continue
            
            plant_type = matrix[i][j]
            patches.append(set())
            explore_q = [(i, j)]
            while explore_q:
                node_i, node_j = explore_q.pop()

                if marked[node_i][node_j]:
                    continue
                
                if matrix[node_i][node_j] == plant_type:
                    patches[-1].add((node_i, node_j))
                    marked[node_i][node_j] = 1

                    for next_explore_node in [(node_i, node_j + 1), (node_i, node_j - 1), (node_i + 1, node_j), (node_i -1, node_j)]:
                        if in_matrix(*next_explore_node, matrix):
                            explore_q.append(next_explore_node)

                else:
                    continue
    
    total = 0
    for patch in patches:
        total += len(patch) * perimeter(patch, matrix)


    return total


def main():
    args = parser.parse_args()
    if args.test:
        print("test input")
        filename = f'{dir}/test_input.txt'
    else:
        filename = f'{dir}/input.txt'

    file = open(filename, 'r')
    lines = [[q for q in l.strip()] for l in file.readlines()]

    print(day_code(lines))


if __name__ == '__main__':
    main()
