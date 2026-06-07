import colorsys, random
from grid import GRID_WIDTH, GRID_HEIGHT, colorGrid, nextColorGrid


def sand_color_generator():
    h = random.uniform(0.08, 0.14)  # ca. gelb/orange Bereich (HSV normalized 0-1)
    s = random.uniform(0.4, 0.7)
    v = random.uniform(0.75, 1.0)

    r, g, b = colorsys.hsv_to_rgb(h, s, v)

    return (
        int(r * 255),
        int(g * 255),
        int(b * 255),
    )


def update_sand(x, y, grid, nextGrid, colorGrid, nextColorGrid):

    is_falling = y < GRID_HEIGHT - 1 and grid[y + 1][x] == 0
    # move one down if space unoccupied
    if is_falling:
        nextGrid[y + 1][x] = 1
        nextColorGrid[y + 1][x] = colorGrid[y][x]
    # if below occupied try moving left
    elif (
        y < GRID_HEIGHT - 1
        and x > 0
        and grid[y + 1][x] == 1
        and grid[y + 1][x - 1] == 0
    ):
        nextGrid[y + 1][x - 1] = 1
        nextColorGrid[y + 1][x - 1] = colorGrid[y][x]
    # if below and left occupied try moving right
    elif (
        y < GRID_HEIGHT - 1
        and x < GRID_WIDTH - 1
        and grid[y + 1][x] == 1
        and grid[y + 1][x + 1] == 0
    ):
        nextGrid[y + 1][x + 1] = 1
        nextColorGrid[y + 1][x + 1] = colorGrid[y][x]
    # otherwise remain on current position
    else:
        nextGrid[y][x] = 1
        nextColorGrid[y][x] = colorGrid[y][x]
