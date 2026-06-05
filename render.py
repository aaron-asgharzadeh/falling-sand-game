import pygame
from grid import grid, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE

COLORS = {0: (0, 0, 0), 1: (194, 178, 128)}  # empty  # sand

nextGrid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
value = 0


def update():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):

            # clear nextGrid to prevent artifacts from earlier states
            nextGrid[y][x] = 0

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            value = grid[y][x]

            # if sand-cell and above bottom of screen
            if value == 1 and y < GRID_HEIGHT - 1:
                nextGrid[y + 1][x] = 1


def commit():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):

            grid[y][x] = nextGrid[y][x]


def draw(screen: pygame.Surface):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):

            value = grid[y][x]
            color = COLORS[value]

            pygame.draw.rect(
                screen,
                color,
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )
