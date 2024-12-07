import argparse
import pathlib
import numpy as np
from operator import *

dir = pathlib.Path(__file__).parent.resolve()

parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')


def concat(a, b):
    return int(str(a)+str(b))


def operator_search(values, cal_value):
    # search items (num a, num b, operator, depth)
    operators = [add, mul, concat]

    search_q = [(values[0], values[1], op, 1) for op in operators]


    while search_q:
        a, b, op, depth = search_q.pop()

        value = op(a,b)

        if value > cal_value:
            continue
        
        if depth == len(values) - 1:
            if value == cal_value:
                return True
            else:
                continue

        
        search_q += [(value, values[depth+1], op, depth+1) for op in operators]

    return False




def day_code(lines):
    count = 0
    for line in lines:
        cal_value, rest = line.split(":")
        values = rest[1:].split(" ")

        cal_value = int(cal_value)
        values = [int(x) for x in values]

        if operator_search(values, cal_value):
            count += cal_value

    return count


                

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
