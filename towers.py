from colours import WHITE
import pygame
vec = pygame.math.Vector2


class Tower:
    def __init__(self, game, surface, x, y, w, h, colour):
        self.surface = surface
        self.position = vec(x, y)
        self.width = w
        self.height = h
        self.game = game
        self.colour = WHITE

    def draw(self):
        pygame.draw.rect(self.surface, self.colour, (self.position.x,
                                                     self.position.y, self.width, self.height), 0)

    def update(self):
        pass
