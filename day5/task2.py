import argparse
import pathlib
import numpy as np

dir = pathlib.Path(__file__).parent.resolve()

parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')

class Rule:
    def __init__(self, X,Y):
        self.x = X
        self.y = Y

        self.hash_ = hash((X,Y))

    def __hash__(self) -> int:
        return self.hash_
    
    def __eq__(self, other):
        return self.hash_ == other.hash_
    

    def follows(self, x, y, i, j):
        return self.x == x and self.y == y and i < j or self.x == y and self.y == x and i > j
    
    def applies(self, x, y):
        return sorted([self.x, self.y]) == sorted([x,y])
    

    def __repr__(self) -> str:
        return (f"{self.x}|{self.y}")



def parse_rules(lines):
    rules = []
    for line in lines:
        if "|" not in line:
            break

        else:
            x,y = line.split("|")
            rules.append(Rule(x,y))
            
    return rules

def parse_manuals(lines):
    manuals = []
    for line in lines:
        if "," not in line:
            continue
        else:
            manuals.append(line.split(','))
    
    return manuals


def fix_manual(manual, rules):
    pages = set(manual)

    matrix = {}

    for page_i in pages:
        matrix[page_i] = {}
        for page_j in pages:
            matrix[page_i][page_j] = Rule(page_i, page_j) in rules

    fixed_manual = []
    removed_pages = set()

    while pages:
        for page in pages:
            if not sum(matrix[page].values()):
                fixed_manual.append(page)
                removed_pages.add(page)

        for page in pages:
            for page_rem in removed_pages:
                matrix[page][page_rem] = 0
        
        pages = pages.difference(removed_pages)

    return fixed_manual

    


def day_code(lines):
    lines = [l.strip() for l in lines]

    rules = parse_rules(lines)
    manuals = parse_manuals(lines)
    
    count = 0

    for manual in manuals:
        good = True

        applying_rules = []
        for i in range(len(manual)):
            for j in range(len(manual)):
                if i == j:
                    continue

                x, y = manual[i], manual[j]

                for rule in rules:
                    if rule.applies(x,y):
                        good &= rule.follows(x,y,i,j)

                        applying_rules.append(rule)
        
        if not good:
            fixed_manual = fix_manual(manual, applying_rules)

            count += int(fixed_manual[len(fixed_manual)//2])
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
