import pygame
from grid import grid, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE

COLORS = {0: (0, 0, 0), 1: (194, 178, 128)}  # empty  # sand

nextGrid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


def update():
    for y in range(GRID_HEIGHT - 1, -1, -1):
        for x in range(GRID_WIDTH):

            # clear nextGrid to prevent artifacts from earlier states
            nextGrid[y][x] = 0

    for y in range(GRID_HEIGHT - 1, -1, -1):
        for x in range(GRID_WIDTH):

            value = grid[y][x]
            is_falling = y < GRID_HEIGHT - 1 and grid[y + 1][x] == 0

            if value == 1:
                # move one down if space unoccupied
                if is_falling:
                    nextGrid[y + 1][x] = 1
                # if below occupied try moving left
                elif (
                    y < GRID_HEIGHT - 1
                    and x > 0
                    # and grid[y + 1][x] == 1
                    and grid[y + 1][x - 1] == 0
                    and nextGrid[y + 1][x] == 1
                ):
                    nextGrid[y + 1][x - 1] = 1
                # if below and left occupied try moving right
                elif (
                    y < GRID_HEIGHT - 1
                    and x < GRID_WIDTH - 1
                    # and grid[y + 1][x] == 1
                    and grid[y + 1][x + 1] == 0
                    and nextGrid[y + 1][x] == 1
                ):
                    nextGrid[y + 1][x + 1] = 1
                # otherwise remain on current position
                else:
                    nextGrid[y][x] = 1


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
