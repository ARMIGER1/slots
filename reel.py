from settings import *
import pygame, random


class Reel:
    def __init__(self, position: tuple[int, int]):
        self.symbol_list = pygame.sprite.Group()
        self.shuffled_keys = list(symbols.keys())
        random.shuffle(self.shuffled_keys)
        self.shuffled_keys = self.shuffled_keys[:5]  # Only matters when there's more than 5 symobols

        self.reel_is_spinning = False

        # Sounds
        self.stop_sound = pygame.mixer.Sound('audio/stop.wav')
        self.stop_sound.set_volume(0.5)

        for idx, item in enumerate(self.shuffled_keys):
            self.symbol_list.add(Symbol(symbols[item], position, idx))
            position = list(position)
            position[1] += 300
            position = tuple(position)


class Symbol(pygame.sprite.Sprite):
    def __init__(self, path: str, position: int, index: int):
        super().__init__()

        # Friendly name
        self.sym_type = path.split('/')[3].split('.')[0]
        self.pos = position
        self.idx = index
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.x_val = self.rect.left

    def update(self):
        pass
