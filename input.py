import pygame
from grid import grid, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT


def handle_input():
    if pygame.mouse.get_pressed()[0]:

        mx, my = pygame.mouse.get_pos()

        x = mx // CELL_SIZE
        y = my // CELL_SIZE

        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            grid[y][x] = 1
