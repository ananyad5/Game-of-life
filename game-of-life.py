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
    return [[random.chocie[0,1] for _ in range(cols)] for _ in range(rows)]


def draw_grid(grid):
    with term.location(0, 0):
        for row in grid:
            line = ''.join(term.green('*') if cell else term.red('.') for cell in row)
            print(line)


def apply_rules(grid, row, col):
    