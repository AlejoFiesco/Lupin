import  pygame
from pygame import *

pygame.init()
screen = pygame.display.set_mode((1320,640))
pygame.display.set_caption("Lupin")
game_running = True
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load("img/bg.png"), (1340,680))

while game_running:
    clock.tick(25)

    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    action = pygame.key.get_pressed()
    pygame.display.update()