import pygame
from player import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    #----Initializeer---
    #===================
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    #----Game Loop---
    #================
    while 1==1:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #print(f"FPS: {dt}")



if __name__ == "__main__":
    main()
