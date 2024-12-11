import argparse
import pathlib
import numpy as np
from operator import *

dir = pathlib.Path(__file__).parent.resolve()

parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')


def in_matrix(i, j, matrix):
    return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])

cache = {}

def populate_cache():
    cache = {}
    for n in range(10):
        print(n)
        cache[n] = {}
        numbers = [n]
        for i in range(75):
            new_numbers = []

            for number in numbers:
                if number == 0:
                    new_numbers.append(1)

                if len(str(number)) % 2 == 0:
                    first_half = str(number)[:len(str(number))//2]
                    second_half = str(number)[len(str(number))//2:]

                    new_numbers.append(int(first_half))
                    new_numbers.append(int(second_half))

                if number != 0 and len(str(number)) %2 != 0:
                    new_numbers.append(number * 2024)

            numbers = new_numbers.copy()
            print(i)


            print(len(numbers))
            cache[n][i] = len(numbers)

    return cache

def day_code(matrix):
    numbers = [int(x) for x in matrix.split(" ")]
    print(numbers)


    for i in range(25):
        new_numbers = []

        for number in numbers:
            if number == 0:
                new_numbers.append(1)

            if len(str(number)) % 2 == 0:
                first_half = str(number)[:len(str(number))//2]
                second_half = str(number)[len(str(number))//2:]

                new_numbers.append(int(first_half))
                new_numbers.append(int(second_half))

            if number != 0 and len(str(number)) %2 != 0:
                new_numbers.append(number * 2024)

        numbers = new_numbers.copy()
        print(i)

    return len(numbers)

def main():
    args = parser.parse_args()
    if args.test:
        print("test input")
        filename = f'{dir}/test_input.txt'
    else:
        filename = f'{dir}/input.txt'

    file = open(filename, 'r')
    lines = [l.strip() for l in file.readlines()][0]

    print(day_code(lines))


if __name__ == '__main__':
    main()
