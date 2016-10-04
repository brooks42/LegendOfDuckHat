
import pygame

class Sprite(pygame.sprite.Sprite):
        """ The Sprite class uses the same design as SQ and some of our other projects,
        basically contains a Surface (for pygame), and a rect for rendering."""

        # takes a spritesheet image and a position to draw at
        # we'll need to do something with initial position because of the way the sprite sheet class works right now,
        # TODO: or we can have the spritesheet start with an initial rectangle, who knows...
        def __init__(self, spritesheet, position):
            pygame.sprite.Sprite.__init__(self,self.groups)
            self.spritesheet = spritesheet
            self.position = position

        def render(screen):
            #screen.blit(image)
