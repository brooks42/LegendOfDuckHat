
import pygame
from GameState import GameState

class TestState(GameState):

    def __init__(self, stateName):
        #creates a default state
        pass

    def update(self, updateObject):
        # updates the game state with the passed deltaT float
        #print(str(updateObject.deltaT))
        #for event in pygame.event.get():
            #if event.type in (QUIT, KEYDOWN):
                #print("we are done")
                #sys.exit()
        pass

    def render(self): # might need to take a parameter? multiple render methods?
        # renders this game state to the screen
        pass
