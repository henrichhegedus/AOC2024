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

    counts = [[0] * n for _ in range(m)]
    
    for robot in robots:
        p, v = robot

        p[0] = (p[0] + v[0] * 100) % m
        p[1] = (p[1] + v[1] * 100) % n

        counts[p[0]][p[1]] += 1

    quadrants = (
        ((0,0), (m//2, n//2)),
        ((m//2 + 1, n//2 +1), (m,n)),
        ((0, n//2 + 1), (m//2, n)),
        ((m//2 + 1, 0), (m, n//2))
        )
    
    total = 1

    for row in counts:
        print("".join([str(x) for x in row]))


    for i_q, q in enumerate(quadrants):
        count = 0
        for i in range(q[0][0], q[1][0]):
            for j in range(q[0][1], q[1][1]):
                count += counts[i][j]

        total *= max(count, 1)
        print(f"quadrant {i_q} has {count} robots")



    return total

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
