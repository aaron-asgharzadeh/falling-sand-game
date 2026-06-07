import pygame
from grid import grid, colorGrid, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE, SAND, WATER
from materials.sand import sand_color_generator

Elements = [SAND, WATER]


def draw(screen: pygame.Surface):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):

            value = grid[y][x]
            if value in Elements:
                color = colorGrid[y][x]
            else:
                color = (0, 0, 0)

            pygame.draw.rect(
                screen,
                color,
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1),
            )
