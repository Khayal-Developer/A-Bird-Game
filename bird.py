import os
import pygame
from pygame.sprite import Sprite

class Bird(pygame.sprite.Sprite):
   def __init__(self, b_game, screen_rect):
       super().__init__()
       # Get the game's screen and settings
       self.screen = b_game.screen
       self.settings = b_game.settings
       self.screen_rect = screen_rect  # Store the screen_rect

       # Get the path to the directory containing the executable
       BASE_DIR = os.path.dirname(os.path.abspath(__file__))

       # Construct the absolute path to the 'images' directory
       IMAGES_DIR = os.path.join(BASE_DIR, 'images')

       # Load the bird image using the absolute path
       self.image = pygame.image.load(os.path.join(IMAGES_DIR, 'bird.png'))
       self.rect = self.image.get_rect()

       # Call the center_bird method to position the bird at the start
       self.center_bird()

       # Set initial movement flags
       self.moving_up = False
       self.moving_down = False

   def update(self):
       """Update the bird's position based on the movement flags."""
       # Update the bird's y-coordinate for up/down movement
       if self.moving_up and self.rect.top > 0:
           self.y -= self.settings.bird_speed
       if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
           self.y += self.settings.bird_speed

       # Update the bird's rect with the new y-coordinate
       self.rect.y = self.y

   def center_bird(self):
       # Center the bird at the left-middle of the screen
       self.rect.midleft = self.screen_rect.midleft

       # Convert the y-coordinate to a float for smoother movement
       self.y = float(self.rect.y)

   def blitme(self):
       # Draw the bird on the screen
       self.screen.blit(self.image, self.rect)