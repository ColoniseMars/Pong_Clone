import pygame
import sys, os
import config

import PongGameScreen

pygame.init()






fpsTime = pygame.time.Clock()
Screen = pygame.display.set_mode((config.window_width, config.window_height))
pygame.display.set_caption(config.gamename)

while True:

    #PongGameScreen.do_tick()
    PongGameScreen.draw(Screen, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsTime.tick(config.fps)