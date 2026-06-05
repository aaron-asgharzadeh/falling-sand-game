import sys, pygame, render
from grid import grid, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE
from input import handle_input
from render import draw, update, commit

render.nextGrid

pygame.init()

SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    handle_input()
    update()
    commit()
    screen.fill((0, 0, 0))  # clear frame
    draw(screen)
    

    pygame.display.flip()
    clock.tick(60)
