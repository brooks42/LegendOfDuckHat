# really simple test game class to help build up functionality quickly

import states.GameState
from states.TestState import TestState
import states.GameUpdate

import pygame

pygame.init()

FPS = 60

def main():
    print("here we go")
    clock = pygame.time.Clock()

    print(type(TestState))
    testState = TestState("test")

    # start the main loop
    while True:
        clock.tick(FPS)

        # detect key presses
        keyPresses = pygame.key.get_pressed()
        #update = states.GameUpdate(10, keyPresses)


if  __name__ =='__main__':main()
