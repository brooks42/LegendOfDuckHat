
"""
The default GameState superclass. Gamestates stack on top of eachother to provide
the UI, effects etc for the game.
"""
class GameState:

    def __init__(self):
        #creates a default state
        pass

    def update(updateObject):
        # updates the game state with the passed deltaT float
        pass

    def render(): # might need to take a parameter? multiple render methods?
        # renders this game state to the screen
        pass
