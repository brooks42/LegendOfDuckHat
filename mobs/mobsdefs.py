
import pygame

# defines a set of information that's used by all mobs in the game
class Mob(Object):

    # initialize a mob
    def __init__(self, sprite):
        self.sprite = sprite;
        self.position = position;

    # render the mob
    def render(screen):
        self.sprite.render(screen)
