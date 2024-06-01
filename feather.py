import os
import pygame
from pygame.sprite import Sprite

class Feather(Sprite):
   def __init__(self, b_game):
       # Call the parent class (Sprite) constructor
       super().__init__()

       # Get the game's screen
       self.screen = b_game.screen  

       # Get the game's settings
       self.settings = b_game.settings  

       # Get the path to the directory containing the executable
       BASE_DIR = os.path.dirname(os.path.abspath(__file__))

       # Construct the absolute path to the 'images' directory
       IMAGES_DIR = os.path.join(BASE_DIR, 'images')

       # Load the bird image using the absolute path
       self.image = pygame.image.load(os.path.join(IMAGES_DIR, 'feather.png'))
       self.rect = self.image.get_rect()  

       # Set the initial position of the feather to the right-middle of the bird
       self.rect.midright = b_game.bird.rect.midright

       # Convert the x-coordinate to a float for smoother movement
       self.x = float(self.rect.x)  

   def update(self):
       # Move the feather horizontally
       # Increase the x-coordinate based on the feather speed
       self.x += self.settings.feather_speed  

       # Update the rectangle's x-coordinate
       self.rect.x = self.x  

   def draw_feather(self):
       # Draw the feather on the screen
       pygame.draw.blit(self.screen, self.rect)