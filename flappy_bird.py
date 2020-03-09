import pygame
import neat
import time
import os
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800


BIRD_IMAGES = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png")))], \
              [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png")))], \
              [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png")))]
PIPE_IMAGE = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))]
BASE_IMAGE = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))]
BG_IMAGE = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))]

class Bird:
    IMAGES = BIRD_IMAGES
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0