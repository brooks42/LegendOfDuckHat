
import sys
import pygame
from pygame.locals import *
from GameState import GameState

class TestState(GameState):

    def __init__(self, stateName):
        #creates a default state
        pass

    def update(self, deltaT):
        # updates the game state with the passed deltaT float
        #print(str(updateObject.deltaT))
        for event in pygame.event.get():
            print("Event: " + str(event))
            if event.type == QUIT or (event.type == KEYDOWN and event.scancode == 9):
                print("we are done")
                sys.exit()

    def render(self): # might need to take a parameter? multiple render methods?
        # renders this game state to the screen
        pass
