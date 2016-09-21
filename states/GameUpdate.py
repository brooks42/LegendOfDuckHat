
class GameUpdate:

    deltaT = 0 # the tick time for the update

    keyPressState = [] # the state of the key presses

    def __init__(self, deltaT, keyPressState):
        self.deltaT = deltaT
        self.keyPressState = keyPressState
