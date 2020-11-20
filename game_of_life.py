# John Conway's Game Of life.
# A simulation of cells in a 2D grid
# driven by a set of rules...

# -------------------------------------------------------------------------------------------------------------------------#

import pygame
from pygame.draw import line, rect
from pygame.time import Clock
from pygame.mouse import get_pos
import random
import numpy as np

# -------------------------------------------------------------------------------------------------------------------------#
width = 600
height = 400
rez = 20
white = (255, 255, 255)
black = (0, 0, 0)
grey = (169, 169, 169)
cols = width // rez
rows = height // rez
# -------------------------------------------------------------------------------------------------------------------------#

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game Of LIfe')

# -------------------------------------------------------------------------------------------------------------------------#

grid = []

for i in range(width // rez):
    grid.append([])
    for j in range(height // rez):
        grid[i].append(0)

# -------------------------------------------------------------------------------------------------------------------------#


def draw_grid():
    for i in range(1, width // rez):
        for j in range(1, height // rez):
            line(display, white, (i * rez, 0), (i * rez, height))
            line(display, white, (0, j * rez), (width, j * rez))

# -------------------------------------------------------------------------------------------------------------------------#


def set_grid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = random.randint(0, 1)

# -------------------------------------------------------------------------------------------------------------------------#


def reset():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = 0

# -------------------------------------------------------------------------------------------------------------------------#


def draw_cells():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            rect(display, (220 * grid[i][j], 220 * grid[i][j],
                           220 * grid[i][j]), (i * rez, j * rez, rez, rez))

# -------------------------------------------------------------------------------------------------------------------------#


def count_neighbours(arr, x, y):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            total += int(arr[x + i][y + j])

    total -= int(arr[x][y])
    return total

# -------------------------------------------------------------------------------------------------------------------------#


def main():
    global grid
    run = True
    clock = Clock()
    set_grid()

    while run:
        clock.tick(7)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                gridpos = grid[get_pos()[0] // rez][get_pos()[1] // rez]
                if gridpos == 0:
                    grid[get_pos()[0] // rez][get_pos()[1] // rez] = 1
                elif gridpos == 1:
                    grid[get_pos()[0] // rez][get_pos()[1] // rez] = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()

        if keys[pygame.K_SPACE]:
            gen = []
            for i in range(width // rez):
                gen.append([])
                for j in range(height // rez):
                    gen[i].append(0)

            for i in range(len(gen)):
                for j in range(len(gen[0])):

                    if (i == 0 or i == cols - 1 or j == 0 or j == rows - 1):
                        gen[i][j] = 0

                    else:
                        state = grid[i][j]
                        neighbours = count_neighbours(grid, i, j)

                        if (state == 0 and neighbours == 3):
                            gen[i][j] = 1
                        elif (state == 1 and (neighbours < 2 or neighbours > 3)):
                            gen[i][j] = 0
                        else:
                            gen[i][j] = state

            grid = gen

        draw_cells()
        draw_grid()
        pygame.display.flip()


# -------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()

# -------------------------------------------------------------------------------------------------------------------------#
