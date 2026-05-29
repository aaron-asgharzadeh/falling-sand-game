import sys, pygame
from grid import grid, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE

COLORS = {0: (0, 0, 0), 1: (194, 178, 128)}  # empty  # sand


def draw(screen: pygame.display.set_mode):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):

            value = grid[y][x]
            color = COLORS[value]

            pygame.draw.rect(
                screen,
                color,
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )
