import argparse
import pathlib
import numpy as np

dir = pathlib.Path(__file__).parent.resolve()

parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')
WORD = "XMAS"


def count_diagonal(matrix, i, j):
    directions = [[1,1], [-1,1], [1,-1], [-1,-1]]
    words = []

    for direction in directions:
        x_dir, y_dir = direction
        letters = []

        for n in range(0, len(WORD)):
            i_i = i + x_dir*n
            j_j = j + y_dir*n
    
            if i_i >= 0 and i_i < len(matrix) and j_j >= 0 and j_j < len(matrix[0]):
                letters.append(matrix[i_i][j_j])
            else:
                letters.append(".")
        
        words.append("".join(letters))
    
    return sum(1 for word in words if WORD == word)


def count_horizontal(matrix, i, j):
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    words = []

    for direction in directions:
        x_dir, y_dir = direction
        letters = []
        y_steps = y_dir * len(WORD) if y_dir != 0 else 1
        x_steps = x_dir * len(WORD) if x_dir != 0 else 1

        for i_i in range(i, i + y_steps, np.sign(y_steps)):
            for j_j in range(j, j + x_steps, np.sign(x_steps)):
                if i_i >= 0 and i_i < len(matrix) and j_j >= 0 and j_j < len(matrix[0]):
                    letters.append(matrix[i_i][j_j])
                else:
                    letters.append(".")
        
        words.append("".join(letters))
    
    return sum(1 for word in words if WORD == word)


def day_code(lines):
    lines = [l.strip() for l in lines]
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            count += count_diagonal(lines, i, j)
            count += count_horizontal(lines, i, j)

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
