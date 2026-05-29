import sys, pygame

pygame.init()

size = width, height = 1377, 768
speed = [1, 1]
black = 0, 0, 0
player_x = 0
player_y = 0
cam_x = 0
cam_y = 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

player = pygame.image.load("intro_ball.gif").convert()

background = pygame.image.load("background.jpeg").convert()
screen.blit(background, (-cam_x, -cam_y))
print(background.get_size())

screen.blit(player, (player_x, player_y))


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # cam_x += 1
    # player_x += 2
    # screen.blit(background, (-cam_x, -cam_y))

    # screen.blit(player, (player_x - cam_x, player_y - cam_y))
    pygame.display.update()
    clock.tick(60)
