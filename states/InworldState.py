
import sys
import pygame
from pygame.locals import *
from GameState import GameState
from window import config

class InworldState(GameState):
    """ The InworldState is the game state we're in when we're playing the game, where
        the user can run around and fight monsters and generally have fun """

    def __init__(self, stateName, screen):
        #creates a default state
        # self.world = initWorld()

        # now load our placeholder art so we can display it
        self.background = pygame.image.load("assets/images/placeholderloadingscreen.png").convert()
        self.background = pygame.transform.scale(self.background, config.resolution)


    def update(self, deltaT):
        # updates the game state with the passed deltaT float
        #print(str(updateObject.deltaT))
        for event in pygame.event.get():
            print("Event: " + str(event))
            # TODO: the config will eventually contain the hotkeys for movement and etc

            if event.type == QUIT or (event.type == KEYDOWN and event.scancode == 9):
                # TODO: eventually replace this with a main menu
                print("we are done")
                sys.exit()

    def render(self, screen): # might need to take a parameter? multiple render methods?
        # renders this game state to the screen
        screen.blit(self.background, (0, 0))
