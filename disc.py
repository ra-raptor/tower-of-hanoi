import random
from colours import *
import pygame
vec = pygame.math.Vector2


class Disc:
    def __init__(self, game, surface, n, max_n, colour):
        self.surface = surface
        self.n = n
        self.colour = colour
        self.animation_stage = 1
        self.game = game
        self.max_n = max_n
        self.calculate_position()

    def calculate_position(self):
        x = (300-120)+(10-self.n)*12
        self.width = 240 - (10-self.n)*24
        self.height = 20
        y = 460 - (self.max_n-self.n)*20
        self.position = vec(x, y)
        print(self.position, self.width, self.width+self.position.x)

    def draw(self):
        pygame.draw.rect(self.surface, self.colour, (self.position.x,
                                                     self.position.y, self.width, self.height), 0)

    def move(self, destination, stage):

        final_x = {
            'A': 300,
            'B': 600,
            'C': 900
        }
        final_tower = {
            'A': self.game.tower_1_count,
            'B': self.game.tower_2_count,
            'C': self.game.tower_3_count
        }
        print(self.animation_stage)
        if(stage == 1):

            if(self.position.y > 150):
                self.position.y -= 5
            if(self.position.y < 155):
                self.position.y = 150
                self.animation_stage = 2
                # stage = 2
        if(stage == 2):
            x_destination = final_x[destination] - (self.width)/2
            if(self.position.x > x_destination):
                self.position.x -= 5
            else:
                self.position.x += 5
            if(self.position.x >= (x_destination-5) or self.position.x >= (x_destination+5)):
                self.position.x = x_destination
                self.animation_stage = 3
        if(stage == 3):
            final_y = 460 - (final_tower[destination])*20
            if(self.position.y < final_y):
                self.position.y += 5
            if(self.position.y > final_y-5):
                self.position.y = final_y
                self.animation_stage = 0

    def update(self):
        self.move('B', self.animation_stage)
        # self.move('C', 2)
