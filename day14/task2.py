import argparse
import pathlib
import numpy as np
from operator import *
from heapq import heappush, heappop, heapify
from tqdm import tqdm
import matplotlib.pyplot as plt


dir = pathlib.Path(__file__).parent.resolve()

parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')


def in_matrix(i, j, matrix):
    return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])

def get_robots(matrix):
    robots = []
    for row in matrix:
        p_str, v_str = row.split(" ")
        p_x = int(p_str.split(",")[0][2:])
        p_y = int(p_str.split(",")[1])

        v_x = int(v_str.split(",")[0][2:])
        v_y = int(v_str.split(",")[1])

        robots.append([[p_x, p_y], [v_x, v_y]])

    return robots


def day_code(matrix, m, n):
    robots = get_robots(matrix)


    for k in tqdm(range(100000), total=100000):
        counts = [[0] * n for _ in range(m)]
        
        for robot in robots:
            p, v = robot

            i = (p[0] + v[0] * k) % m
            j = (p[1] + v[1] * k) % n

            counts[i][j] = 1


        any_neighbours = False
        for i in range(m):
            for j in range(n):
                neighbours = True

                for i_i in range(i-2, i+2):
                    for j_j in range(j-2, j+2):
                        if not in_matrix(i_i, j_j, counts) or not counts[i_i][j_j]:
                            neighbours = False
                            break
                
                    if not neighbours:
                        break
                
                any_neighbours |= neighbours
                

        if any_neighbours:
            plt.imsave(f"{dir}/images/{k:05}.png", counts)
            break


def main():
    args = parser.parse_args()
    if args.test:
        print("test input")
        filename = f'{dir}/test_input.txt'
        m, n = 7, 11
    else:
        filename = f'{dir}/input.txt'
        m, n = 101, 103

    file = open(filename, 'r')
    lines = [l.strip() for l in file.readlines()]

    print(day_code(lines, m, n))


if __name__ == '__main__':
    main()
