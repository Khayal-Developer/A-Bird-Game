import os
import pygame

class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700

        # Get the path to the directory containing the executable
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute path to the 'images' directory
        IMAGES_DIR = os.path.join(BASE_DIR, 'images')

        # Load the background image using the absolute path
        self.screen_bg_colour = pygame.image.load(os.path.join(IMAGES_DIR, 'background.bmp'))
        self.bg_colour_rect = self.screen_bg_colour.get_rect()

        # Bird settings
        self.bird_speed = 3.0
        self.bird_limit = 3

        # Feather settings
        self.feather_speed = 5.0
        self.feathers_allowed = 5

        # Monster settings
        self.monster_frequency = 0.008
        self.monster_speed = 1.5