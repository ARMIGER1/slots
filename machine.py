from settings import *
from reel import *

import pygame

class Machine:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.reel_index = 0
        self.reel_list = {}

        self.spawn_reels()

    def spawn_reels(self):
        if not self.reel_list:
            x_top_left, y_top_left = 10, -300
            while self.reel_index < 5:
                if self.reel_index > 0:
                    x_top_left, y_top_left = x_top_left + (300 + X_OFFSET), y_top_left

                self.reel_list[self.reel_index] = Reel((x_top_left, y_top_left)) # TODO: Create Reel class
                self.reel_index += 1

    def update(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()