
import random
import pygame
pygame.init()

width = 900
height = 600
rez = 18
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Of Life")
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def draw_board(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 1:
                pygame.draw.rect(display, (220, 220, 220), (c * rez, r * rez, rez, rez))
            else:
                pygame.draw.rect(display, (0, 0, 0), (c * rez, r * rez, rez, rez), 2)

def gol(board):
    next_gen = [[0 for _ in range(width // rez)] for _ in range(height // rez)]
    for r in range(1, len(board) - 1):
        for c in range(1, len(board[0]) - 1):
            neighbors = 0
            state = board[r][c]

            for dr, dc in dirs:
                neighbors += board[r + dr][c + dc]

            if (neighbors == 3) and (state == 0):
                next_gen[r][c] = 1

            elif (neighbors > 3 or neighbors < 2) and state == 1:
                next_gen[r][c] = 0

            else:
                next_gen[r][c] = state

    return next_gen

def main():
    loop = True
    board = [[0 for _ in range(width // rez)] for _ in range(height // rez)]

    # plane
    board[5][5] = 1
    board[6][6] = 1
    board[7][4] = 1
    board[7][5] = 1
    board[7][6] = 1



    clock = pygame.time.Clock()
    toggle = False

    while loop:
        clock.tick(10)
        display.fill((20, 20, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                # quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                (y, x) = pygame.mouse.get_pos()
                y = y // rez
                x = x // rez

                board[x][y] = 1 if board[x][y] == 0 else 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    toggle = not toggle

                if event.key == pygame.K_r:
                    board = [[0 for _ in range(width // rez)] for _ in range(height // rez)]

        if toggle:
            board = gol(board)

        draw_board(board)
        pygame.display.flip()


if __name__ == "__main__":
    main()

