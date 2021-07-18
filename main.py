import random
from colours import *
from towers import Tower
from disc import Disc
import pygame
pygame.init()


class Game:
    def __init__(self):
        self.WIDTH = 1200
        self.HEIGHT = 600
        self.TITLE = "Tower of Hanoi"
        self.FPS = 60
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.TITLE)
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.run()

    def run(self):
        self.disc_group = []
        self.ready()
        while self.is_running:
            self.clock.tick(self.FPS)
            self.dt = self.clock.tick(self.FPS)/1000

            self.events()
            self.update()
            self.draw()

    def ready(self):
        self.create_towers()
        self.create_discs()

    def create_towers(self):
        self.tower_1 = Tower(self, self.screen, 298, 280, 4, 200, WHITE)
        self.tower_2 = Tower(self, self.screen, 598, 280, 4, 200, WHITE)
        self.tower_3 = Tower(self, self.screen, 898, 280, 4, 200, WHITE)

    def create_discs(self):
        disc_count = 3
        self.tower_1_count = disc_count
        self.tower_2_count = 0
        self.tower_3_count = 0
        for i in range(disc_count):
            col = random.choice(
                [RED, GREEN, GOLD, LIME, CYAN, SAND, YELLOW, SALMON, DARKGREEN, NAVYBLUE])
            disc = Disc(self, self.screen, i+1, disc_count, col)
            self.disc_group.append(disc)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        self.disc_group[0].update()
        # self.disc_group[1].update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (255, 255, 255), (150, 480, 900, 8))
        self.tower_1.draw()
        self.tower_2.draw()
        self.tower_3.draw()
        for disc in self.disc_group:
            disc.draw()
        # pygame.draw.rect(self.screen, GREEN, (175, 460, 250, 20))
        # pygame.draw.rect(self.screen, RED, (475, 460, 250, 20))
        # pygame.draw.rect(self.screen, GREEN, (775, 460, 250, 20))
        pygame.display.update()


if __name__ == "__main__":
    Game()
    pygame.quit()
    pygame.display.quit()
