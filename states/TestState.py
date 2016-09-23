
from GameState import GameState

class TestState(GameState):

    def __init__(self, stateName):
        #creates a default state
        pass

    def update(self, updateObject):
        # updates the game state with the passed deltaT float
        print(str(updateObject.deltaT))

    def render(self): # might need to take a parameter? multiple render methods?
        # renders this game state to the screen
        pass
