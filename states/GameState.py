
"""
The default GameState superclass. Gamestates stack on top of eachother to provide
the UI, effects etc for the game.
"""
class GameState:

    def __init__(self):
        #creates a default state
        pass

    def update(self, deltaT):
        # updates the game state with the passed deltaT float
        pass

    def render(self): # might need to take a parameter? multiple render methods?
        # renders this game state to the screen
        # from what I understand of pygame we'll have to blit all of the sprites on the screen in this state.
        # should we have a RenderState or something to render only things that have to be done?
        pass
