import sys, pygame
from grid import grid, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE
from input import handle_input
from render import draw, update, commit

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
    screen.fill((0, 0, 0))  # clear frame
    draw(screen)
    update()
    commit()

    pygame.display.flip()
    clock.tick(60)
