import pygame
from grid import grid, colorGrid, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT, SAND, WATER
from materials.sand import sand_color_generator
from materials.water import water_color_generator


def spawn_sand(x, y):
    if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
        grid[y][x] = SAND
        colorGrid[y][x] = sand_color_generator()


def spawn_water(x, y):
    if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
        grid[y][x] = WATER
        colorGrid[y][x] = water_color_generator()


def handle_input():
    if pygame.mouse.get_pressed()[0]:

        mx, my = pygame.mouse.get_pos()

        x = mx // CELL_SIZE
        y = my // CELL_SIZE

        spawn_sand(x, y)
        print("Links")

    elif pygame.mouse.get_pressed()[2]:

        mx, my = pygame.mouse.get_pos()

        x = mx // CELL_SIZE
        y = my // CELL_SIZE

        spawn_water(x, y)
        print("Rechts")
