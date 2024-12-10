import argparse
import pathlib
import numpy as np
from operator import *

dir = pathlib.Path(__file__).parent.resolve()

parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')


def in_matrix(i, j, matrix):
    return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])


def construct_array(line):
    array = []

    free = False
    index = 0

    for i in line:
        if not free:
            array += [index] * i
            free = True
            index += 1
        else:
            array += [-1] * i
            free = False

    return array

        



def day_code(lines):
    array = construct_array(lines)
    print(array)

    i = 0
    j = len(array) -1

    while i <= j:
        while array[i] != -1:
            i += 1

        while array[j] == -1:
            j -= 1

        if i > j:
            break

        print(i,j)
        array[i], array[j] = array[j], array[i]


    print([(i,e) for i,e in enumerate(array)])

    checksum = 0

    for i, id in enumerate(array):
        if id == -1:
            break
    
        checksum += i*id
    
    return checksum

        




                

def main():
    args = parser.parse_args()
    if args.test:
        print("test input")
        filename = f'{dir}/test_input.txt'
    else:
        filename = f'{dir}/input.txt'

    file = open(filename, 'r')
    lines = [[int(x) for x in l.strip()] for l in file.readlines()][0]

    print(day_code(lines))


if __name__ == '__main__':
    main()
