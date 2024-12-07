import argparse
import pathlib
import numpy as np

dir = pathlib.Path(__file__).parent.resolve()

parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')
WORD = "XMAS"


PATTERNS = [
"""
M.M
.A.
S.S
""",
"""
S.S
.A.
M.M
""",
"""
S.M
.A.
S.M
""",
"""
M.S
.A.
M.S
"""
]


def match(matrix, i, j):
    count = 0
    for pattern in PATTERNS:
        pattern_m = pattern.splitlines()[1:]
        
        match = True
        for i_i in range(0, len(pattern_m)):
            for j_j in range(0, len(pattern_m[0])):
                try:
                    if matrix[i+i_i][j+j_j] == pattern_m[i_i][j_j] or pattern_m[i_i][j_j] == ".":
                        continue
                    else:
                        match = False
                        break
                except:
                    match = False
                    break
            if not match:
                break

        count += match
    return count
    


def day_code(lines):
    lines = [l.strip() for l in lines]
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            count += match(lines, i, j)

    return count

def main():
    args = parser.parse_args()
    if args.test:
        print("test input")
        filename = f'{dir}/test_input.txt'
    else:
        filename = f'{dir}/input.txt'

    file = open(filename, 'r')
    lines = file.readlines()

    print(day_code(lines))


if __name__ == '__main__':
    main()
