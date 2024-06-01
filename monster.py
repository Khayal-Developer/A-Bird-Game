import os
# Import the randint function from the random module
from random import randint 

# Import the Pygame library
import pygame  

# Import the Sprite class from the Pygame sprite module
from pygame.sprite import Sprite  

class Monster(Sprite):
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
        self.image = pygame.image.load(os.path.join(IMAGES_DIR, 'monster.png'))
        self.rect = self.image.get_rect()  

        # Set the initial position of the monster on the right side of the screen
        self.rect.left = self.screen.get_rect().right

        # Calculate the maximum top position for the monster, ensuring it doesn't go off the screen
        monster_top_max = self.settings.screen_height - self.rect.height

        # Set a random top position for the monster
        self.rect.top = randint(0, monster_top_max)  

        # Convert the x-coordinate to a float for smoother movement
        self.x = float(self.rect.x)  

    def update(self):
        # Move the monster horizontally
        # Decrease the x-coordinate based on the monster speed
        self.x -= self.settings.monster_speed  

        # Update the rectangle's x-coordinate
        self.rect.x = self.x  