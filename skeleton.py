import argparse


parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')


def day_code(lines):
    return 0


def main():
    args = parser.parse_args()
    if args.test:
        filename = 'test_input.txt'
    else:
        filename = 'input.txt'

    file = open(filename, 'r')
    lines = file.readlines()

    print(day_code(lines))


if __name__ == '__main__':
    main()
