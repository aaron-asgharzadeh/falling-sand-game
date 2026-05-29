import sys, pygame
from grid import grid, GRID_WIDTH, GRID_HEIGHT
from input import handle_input
from render import draw

pygame.init()

screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    handle_input()

    screen.fill((0, 0, 0))  # clear frame
    draw(screen)

    pygame.display.flip()
    clock.tick(60)
