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
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMAGES[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d = self.vel*self.tick_count + 1.5*self.tick_count**2
        # -10.5 + 1.5 = -9
        if d >= 16:
            d = 16

        if d < 0:
            d -= 2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL
    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMAGES[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMAGES[1]
        elif  self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMAGES[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMAGES[1]
        elif self.img_count < self.ANIMATION_TIME*4 + 1:
            self.img = self.IMAGES[0]
            self.img_count = 0