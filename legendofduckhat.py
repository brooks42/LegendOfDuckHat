# the main file of the game, can be run with
# python gamerun.py

import time
from window import config
from states.InworldState import InworldState
from states.update import GameUpdate

import pygame

pygame.init()

def main():
    print("here we go")
    clock = pygame.time.Clock()

    lastTime = time.clock()

    # initialize our screen...
    screen = pygame.display.set_mode(config.resolution, pygame.FULLSCREEN)

    # initialize the ingame state here, we have to pass the screen in to give it
    # our config options
    testState = InworldState("test", screen)

    # start the main loop
    while True:
        clock.tick(config.FPS)

        thisTime = time.clock()
        deltaT = thisTime - lastTime
        lastTime = thisTime

        # detect key presses
        testState.update(deltaT)

        # render loop I guess
        pygame.display.update()
        testState.render(screen)


if  __name__ =='__main__':
    main()
