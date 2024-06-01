import os
import pygame
from random import randint, choice
import time

class StaticStar(pygame.sprite.Sprite):
    def __init__(self, b_game):
        # Call the parent class constructor
        super().__init__()

        self.screen = b_game.screen
        self.screen_rect = self.screen.get_rect()

        # Get the path to the directory containing the executable
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute path to the 'images' directory
        IMAGES_DIR = os.path.join(BASE_DIR, 'images')


        # Load the bird image using the absolute path
        self.image = pygame.image.load(os.path.join(IMAGES_DIR, 'star_02.png'))
        self.rect = self.image.get_rect()

        # Set the initial position of the star randomly
        self.rect.x = randint(0, self.screen_rect.width - self.rect.width)
        self.rect.y = randint(0, self.screen_rect.height - self.rect.height)

    def blit(self):
        # Draw the star on the screen
        self.screen.blit(self.image, self.rect)

class BlinkingStar(pygame.sprite.Sprite):
    def __init__(self, game):
        # Call the parent class constructor
        super().__init__()

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Get the path to the directory containing the executable
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute path to the 'images' directory
        IMAGES_DIR = os.path.join(BASE_DIR, 'images')

        # Load the bird image using the absolute path
        self.image = pygame.image.load(os.path.join(IMAGES_DIR, 'star.png'))
        self.rect = self.image.get_rect()

        # Set the initial position of the star randomly
        self.rect.x = randint(0, self.screen_rect.width - self.rect.width)
        self.rect.y = randint(0, self.screen_rect.height - self.rect.height)

        # Set the timer for the star to appear and disappear
        self.appear_time = time.time()
        self.appear_duration = randint(2, 5)  # Random duration between 2-5 seconds
        self.disappear_duration = randint(2, 5)  # Random duration between 2-5 seconds

    def update(self):
        # Get the current time
        now = time.time()

        # Check if the star should appear or disappear
        if now - self.appear_time < self.appear_duration:
            self.blit()
        elif self.appear_duration <= now - self.appear_time < self.appear_duration + self.disappear_duration:
            pass  # Do nothing (star is invisible)
        else:
            self.appear_time = now
            self.rect.x = randint(0, self.screen_rect.width - self.rect.width)
            self.rect.y = randint(0, self.screen_rect.height - self.rect.height)
            self.appear_duration = randint(2, 5)
            self.disappear_duration = randint(2, 5)

    def blit(self):
        # Draw the star on the screen
        self.screen.blit(self.image, self.rect)