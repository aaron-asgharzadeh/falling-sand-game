import pygame
from grid import grid, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT

prev_x = None
prev_y = None


def handle_input():
    global prev_x, prev_y
    if pygame.mouse.get_pressed()[0]:

        mx, my = pygame.mouse.get_pos()

        x = mx // CELL_SIZE
        y = my // CELL_SIZE

        if prev_x is not None:
            steps = max(abs(x - prev_x), abs(y - prev_y))

            for i in range(steps):
                ix = prev_x + (x - prev_x) * i // steps
                iy = prev_y + (y - prev_y) * i // steps

                if 0 <= ix < GRID_WIDTH and 0 <= iy < GRID_HEIGHT:
                    grid[iy][ix] = 1

        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            grid[y][x] = 1

        prev_x, prev_y = x, y
    else:
        prev_x, prev_y = None, None
