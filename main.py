from colours import WHITE
from towers import Tower
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
        while self.is_running:
            self.clock.tick(self.FPS)
            self.dt = self.clock.tick(self.FPS)/1000
            self.ready()
            self.events()
            self.updates()
            self.draw()

    def ready(self):
        self.create_towers()

    def create_towers(self):
        self.tower_1 = Tower(self, self.screen, 296, 280, 8, 200, WHITE)
        self.tower_2 = Tower(self, self.screen, 596, 280, 8, 200, WHITE)
        self.tower_3 = Tower(self, self.screen, 896, 280, 8, 200, WHITE)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def updates(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (255, 255, 255), (150, 480, 900, 8))
        self.tower_1.draw()
        self.tower_2.draw()
        self.tower_3.draw()
        pygame.display.update()


if __name__ == "__main__":
    Game()
    pygame.quit()
    pygame.display.quit()
