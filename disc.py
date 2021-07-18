import random
from colours import *
import pygame
vec = pygame.math.Vector2


class Disc:
    def __init__(self, game, surface, n, max_n, colour):
        self.surface = surface
        self.n = n
        self.colour = colour

        self.game = game
        self.max_n = max_n
        self.calculate_position()

    def calculate_position(self):
        x = (300-120)+(10-self.n)*12
        self.width = 240 - (10-self.n)*24
        self.height = 20
        y = 460 - (self.max_n-self.n)*20
        self.position = vec(x, y)

    def draw(self):
        pygame.draw.rect(self.surface, self.colour, (self.position.x,
                                                     self.position.y, self.width, self.height), 0)

    def move(self, original, destination):
        if(original == 'A'):
            if(destination == 'B'):
                pass

    def update(self):
        pass
