import argparse
import pathlib
import numpy as np
from operator import *

dir = pathlib.Path(__file__).parent.resolve()

parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')


def in_matrix(i, j, matrix):
    return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])


def show_antinodes(antinodes):
    for row in antinodes:
        row = "".join(["X" if antinode else "." for antinode in row])
        print(row)


def day_code(lines):
    count = 0
    m, n = len(lines), len(lines[0])

    nodes = {}

    for i in range(m):
        for j in range(n):
            node = lines[i][j]

            if node == ".":
                continue

            if not node in nodes:
                nodes[node] = []

            nodes[node].append((i, j))


    antinodes = [[0]*n for _ in range(m)]

    for _, node_list in nodes.items():
        for i in range(len(node_list)-1):
            for j in range(i + 1, len(node_list)):
                node_a = node_list[i]
                node_b = node_list[j]

                diff_i = node_b[0] - node_a[0]
                diff_j = node_b[1] - node_a[1]

                pos1 = (node_a[0] - diff_i, node_a[1] - diff_j)
                pos2 = (node_b[0] + diff_i, node_b[1] + diff_j)


                t = 0
                pos1 = (node_a[0] - t * diff_i, node_a[1] - t * diff_j)
                while in_matrix(*pos1, lines):
                    antinodes[pos1[0]][pos1[1]] = 1

                    pos1 = (node_a[0] - t * diff_i, node_a[1] - t *diff_j)
                    t +=1


                
                t = 0
                pos2 = (node_b[0] + t* diff_i, node_b[1] + t * diff_j)
                while in_matrix(*pos2, lines):
                    antinodes[pos2[0]][pos2[1]] = 1


                    pos2 = (node_b[0] + t* diff_i, node_b[1] + t * diff_j)
                    t +=1


    show_antinodes(antinodes)

    return sum([sum(x) for x in antinodes])





                

def main():
    args = parser.parse_args()
    if args.test:
        print("test input")
        filename = f'{dir}/test_input.txt'
    else:
        filename = f'{dir}/input.txt'

    file = open(filename, 'r')
    lines = [[x for x in l.strip()] for l in file.readlines()]

    print(day_code(lines))


if __name__ == '__main__':
    main()
