import argparse
import pathlib

dir = pathlib.Path(__file__).parent.resolve()

parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')

from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap


#####################
#       CODE        #
#####################

cache = {}

def recursive_step(number, depth):
    global cache

    if cache.get(number, {}).get(depth, False):
        return cache[number][depth]

    if depth == 75:
        return 1

    new_numbers = []

    if number == 0:
        new_numbers.append(1)

    if len(str(number)) % 2 == 0:
        first_half = str(number)[:len(str(number)) // 2]
        second_half = str(number)[len(str(number)) // 2:]

        new_numbers.append(int(first_half))
        new_numbers.append(int(second_half))

    if number != 0 and len(str(number)) % 2 != 0:
        new_numbers.append(number * 2024)

    children_count = sum([recursive_step(n, depth + 1) for n in new_numbers])

    if number not in cache: cache[number] = {}
    cache[number][depth] = children_count
    return children_count

@timing
def day_code(matrix):
    numbers = [int(x) for x in matrix.split(" ")]

    return   sum([recursive_step(number, 0) for number in numbers])

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
