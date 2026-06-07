from grid import grid, nextGrid, colorGrid, nextColorGrid, GRID_WIDTH, GRID_HEIGHT
from materials import UPDATERS


def update():
    for y in range(GRID_HEIGHT - 1, -1, -1):
        for x in range(GRID_WIDTH):

            # clear nextGrid to prevent artifacts from earlier states
            nextGrid[y][x] = 0
            nextColorGrid[y][x] = (0, 0, 0)

    for y in range(GRID_HEIGHT - 1, -1, -1):
        for x in range(GRID_WIDTH):

            value = grid[y][x]

            if value in UPDATERS:
                UPDATERS[value](x, y, grid, nextGrid, colorGrid, nextColorGrid)


def commit():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):

            grid[y][x] = nextGrid[y][x]
            colorGrid[y][x] = nextColorGrid[y][x]
