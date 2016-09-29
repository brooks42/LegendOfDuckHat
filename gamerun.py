# really simple test game class to help build up functionality quickly

import time
from window import config
from states.TestState import TestState
from states.update import GameUpdate

import pygame

pygame.init()

def main():
    print("here we go")
    clock = pygame.time.Clock()

    testState = TestState("test")

    lastTime = time.clock()

    # initialize our screen...
    screen = pygame.display.set_mode(config.resolution)

    # now load our placeholder art so we can display it
    background = pygame.image.load("assets/images/placeholderloadingscreen.png").convert()
    background = pygame.transform.scale(background, config.resolution)

    # start the main loop
    while True:
        clock.tick(config.FPS)

        thisTime = time.clock()
        deltaT = thisTime - lastTime
        lastTime = thisTime

        # detect key presses
        keyPresses = pygame.key.get_pressed()
        update = GameUpdate(deltaT, keyPresses)
        testState.update(update)

        # render loop I guess
        screen.blit(background, (0, 0))
        pygame.display.update()


if  __name__ =='__main__':main()
