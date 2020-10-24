import pygame
import numpy
import random
import math

width = 600
height = 600
rez = 20
rows = width // rez
cols = height // rez

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game Of Life')

grid = numpy.empty(shape = (width // rez, height // rez))
gen = numpy.empty(shape = (width // rez, height // rez))


for i in range(len(grid)):
    for j in range(len(grid[0])):
        grid[i][j] = math.floor(random.randint(0 ,1))


def count(arr, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (-1 < i + x < len(grid) and -1 < j + y < len(grid[0])):
                sum += arr[x + i][y + j]
    sum -= grid[x][y]
    return sum


def main():
    run = True

    while run:
        gen = grid

        for i in range(len(gen)):
            for j in range(len(gen[0])):

                if (i == 0 or i == cols - 1 or j == 0 or j == rows - 1):
                    grid[i][j] = gen[i][j]

                else:
                    neighbours = count(gen, i, j)
                    state = gen[i][j]

                    if (state == 0 and neighbours == 3):
                        grid[i][j] = 1
                    elif (state == 1 and (neighbours < 2 or neighbours > 3)):
                        grid[i][j] = 0
                    else:
                        grid[i][j] = state

    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    pygame.draw.rect(display, (255, 255, 255), (i * rez, j * rez, rez, rez))
                elif grid[i][j] == 0:
                    pygame.draw.rect(display, (0, 0, 0), (i * rez, j * rez, rez, rez))


        for i in range(1, height // rez):
            pygame.draw.line(display, (169,  169, 169), (0, i * rez), (width, i * rez))

        for j in range(1, width // rez):
            pygame.draw.line(display, (169,  169, 169), (j * rez, 0), (j * rez, height))

        pygame.display.update()

main()

