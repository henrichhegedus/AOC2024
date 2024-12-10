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


def get_free_spots(array):
    free_spots = []

    for i, e in enumerate(array):
        if i == 0:
            pass
        
        if array[i-1] != -1 and e == -1:
            free_spots.append([i, 1])

        if array[i-1] == -1 and e == -1:
            free_spots[-1][1] += 1

    return free_spots
            



def day_code(lines):
    array = construct_array(lines)
    free_spots = get_free_spots(array)
    print(array)
    print(free_spots)

    i = len(array) -2
    j = len(array) -1

    while i >= -1:
        if array[i] == array[j]:
            i -= 1
            continue

        if array[i] != array[j]:
            length = j-i


            if array[j] != -1:
                start_i = i + 1
                for l, (start_free, len_free) in enumerate(free_spots):
                    if start_free + len_free < j and len_free >= length:
                        for k in range(length):
                            array[start_free + k], array[start_i + k] = array[start_i + k], -1
                            free_spots[l] = [start_free + k + 1, len_free - length]
                        
                        break

            j = i

        i -= 1
        
    print(array)


    checksum = 0

    for i, id in enumerate(array):
        if id == -1:
            continue
    
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
