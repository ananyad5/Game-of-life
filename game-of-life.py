from blessed import Terminal
import time
import os
import random 

term = Terminal()

ALIVE = '*'
DEAD = '.'

rows = 20
cols = 20

# creating and drawing a grid with * as alive cells and . as dead
def initial_grid():
    return [[random.choice[0,1] for _ in range(cols)] for _ in range(rows)]


def draw_grid(grid):
    with term.location(0, 0):
        for row in grid:
            line = ''.join(term.green('*') if cell else term.red('.') for cell in row)
            print(line)


def apply_rules(grid, row, col):
    if row -1 and col - 1:
        if grid[row-1][col-1] != 1:
            alive += 1

def update_grid(grid):
    for row in grid:
        for col in row:
            grid[row][col] = apply_rules(grid, row, col)


def main():
    grid =  initial_grid()
    new = draw_grid(grid)