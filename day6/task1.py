import argparse
import pathlib
import numpy as np
from operator import *

dir = pathlib.Path(__file__).parent.resolve()

parser = argparse.ArgumentParser(description='Advent of code')
parser.add_argument('-t', '--test', help='run on test file', action='store_true')




class Agent:
    def __init__(self, board):
        self.board  = board
        self.position = self.find_agent()
        self.direction = [-1,0]
        self.on_board = True

        self.board_dim_i = len(board)
        self.board_dim_j = len(board[0])

    def find_agent(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == "^":
                    return [i,j]

    def rotate(self):
        if self.direction == [-1, 0]:
            self.direction = [0, 1]
        elif self.direction == [0,1]:
            self.direction = [1,0]
        elif self.direction == [1,0]:
            self.direction = [0, -1]
        elif self.direction == [0, -1]:
            self.direction = [-1, 0]

    def move(self):
        next_i, next_j = map(add, self.position, self.direction)
        
        if next_i < 0 or next_j < 0:
            self.on_board = False
            return

        try:
            if self.board[next_i][next_j] == "#":
                self.rotate()
            elif self.board[next_i][next_j] != "#":
                self.position = [next_i, next_j]
        except Exception:
            self.on_board = False
            
    @property
    def pose(self):
        return *self.position, *self.direction

def day_code(lines):
    agent = Agent(lines)


    poses = []
    visited = [[0]*len(lines[0]) for _ in range(len(lines))]

    while agent.on_board:
        i, j = agent.position
        visited[i][j] = 1

        if agent.pose in poses:
            break

        poses.append(agent.pose)
            

        agent.move()
    for i, vi in enumerate(visited):
        obstacles = ["#" if x == "#" else " " for x in lines[i]]
        vi = ["X" if x else " " for x in vi]

        combine = []

        for j in range(len(obstacles)):
            if obstacles[j] != " ":
                combine.append(obstacles[j])
            else:
                combine.append(vi[j])

        print("".join(combine))
    return sum([sum(row) for row in visited])
                

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
