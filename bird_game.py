# Import the sys module to allow exiting the game
import sys  

# Import the random function to generate random numbers
from random import random  

# Import the Pygame library
import pygame  

# Import the necessary classes from other files
from settings import Settings
from game_stats import GameStats
from button import PlayButton, ExitButton
from bird import Bird
from feather import Feather
from monster import Monster
from star import StaticStar, BlinkingStar


class BirdGame():
    def __init__(self):
        pygame.init()  # Initialize Pygame
        self.clock = pygame.time.Clock()  # Create a clock object to control the frame rate
        self.settings = Settings()  # Create an instance of the Settings class

        # Set up the game window in fullscreen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().w  # Get the width of the screen
        self.settings.screen_height = self.screen.get_rect().h  # Get the height of the screen
        pygame.display.set_caption('A Bird Game')  # Set the title of the game window

        self.stats = GameStats(self)  # Create an instance of the GameStats class

        # ... (other initialization code)
        self.bird = Bird(self, self.screen.get_rect())  # Pass self.screen.get_rect() to the Bird instance
        self.feathers = pygame.sprite.Group()  # Create a group to store feathers
        self.monsters = pygame.sprite.Group()  # Create a group to store monsters
        self.static_stars = pygame.sprite.Group()  # Create a group to store static stars

        # Create 35 static stars and add them to the group
        for _ in range(35):
            star = StaticStar(self)
            self.static_stars.add(star)

        # Create a group to store blinking stars
        self.blinking_stars = pygame.sprite.Group()  
        
        # Create 10 blinking stars and add them to the group
        for _ in range(15):
            star = BlinkingStar(self)
            self.blinking_stars.add(star)


        # Set the initial game state to inactive
        self.game_active = False
        # Create an instance of the Button class with the text "Play"  
        self.play_button = PlayButton(self, "Play", y_offset=50)
        # Create an exit button positioned 100 pixels below the center
        self.exit_button = ExitButton(self, "Exit", y_offset=30)

    def run_game(self):
        while True:
            self._all_events()  # Check for events (e.g., user input, quit)

            if self.game_active:
                self._create_monster()  # Create a new monster if conditions are met
                self.blinking_stars.update()  # Update the blinking stars
                self.bird.update()  # Update the bird's position
                self.monsters.update()  # Update the monsters' positions
                self._update_feathers()  # Update the feathers' positions
                self._update_monsters()  # Update the monsters and check for collisions
                

            self._update_screen()  # Update the screen display
            self.clock.tick(60)  # Limit the frame rate to 60 FPS

    def _all_events(self):
        # Loop through all the events that happened since the last frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # Exit the game if the user closes the window
            elif event.type == pygame.KEYDOWN:
                self._active_events(event)  # Handle key press events
            elif event.type == pygame.KEYUP:
                self._passive_events(event)  # Handle key release events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # Get the position of the mouse cursor
                # Check if the play button was clicked
                self._check_play_button(mouse_pos)
                # Check if the exit button was clicked
                self.exit_button.check_click(mouse_pos)

    def _active_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.bird.moving_up = True  # Move the bird up
        elif event.key == pygame.K_DOWN:
            self.bird.moving_down = True  # Move the bird down
        elif event.key == pygame.K_SPACE:
            self._fire_feather()  # Fire a new feather

    def _passive_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_UP:
            self.bird.moving_up = False  # Stop moving the bird up
        elif event.key == pygame.K_DOWN:
            self.bird.moving_down = False  # Stop moving the bird down

    def _check_play_button(self, mouse_pos):
        # Check if the mouse cursor is over the play button
        button_clicked =  self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game statistics
            self.stats.reset_stats()
            self.game_active = True  # Set the game to active

            # Get rid of any remaining feathers and monsters
            self.feathers.empty()
            self.monsters.empty()

            # Create new monsters
            self._create_monster()
            # Center the bird
            self.bird.center_bird()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)

    def _fire_feather(self):
        # Check if the maximum number of feathers is not reached
        if len(self.feathers) < self.settings.feathers_allowed:
            new_feather = Feather(self)  # Create a new feather
            self.feathers.add(new_feather)  # Add the new feather to the group

    def _update_feathers(self):
        self.feathers.update()  # Update the positions of all feathers

        # Remove any feathers that have gone off the screen
        for feather in self.feathers.copy():
            if feather.rect.left >= self.screen.get_rect().right:
                self.feathers.remove(feather)

        self._check_feather_monster_collisions()  # Check for collisions between feathers and monsters

    def _check_feather_monster_collisions(self):
        # Check for collisions between feathers and monsters, and remove them if they collide
        collisions = pygame.sprite.groupcollide(self.feathers, self.monsters, True, True)

    def _create_monster(self):
        # Create a new monster based on the monster frequency setting
        if random() < self.settings.monster_frequency:
            monster = Monster(self)
            self.monsters.add(monster)

    def _update_monsters(self):
        self.monsters.update()  # Update the positions of all monsters

        # Check if the bird collided with any monster
        if pygame.sprite.spritecollideany(self.bird, self.monsters):
            self._bird_hit()

        self._check_monsters_left_edge()  # Check if any monster has gone off the left edge of the screen

    def _check_monsters_left_edge(self):
        # Loop through all monsters
        for monster in self.monsters.sprites():
            if monster.rect.left < 0:
                self._bird_hit()  # Call the _bird_hit method if a monster has gone off the left edge
                break  # Exit the loop after the first monster that went off the edge

    def _bird_hit(self):
        if self.stats.birds_left > 0:
            self.stats.birds_left -= 1  # Decrement the number of birds left
        else:
            self.game_active = False  # End the game if there are no birds left
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        # Draw the background color
        self.screen.blit(self.settings.screen_bg_colour, self.settings.bg_colour_rect)

        # Draw all game objects
        self.feathers.draw(self.screen)
        self.static_stars.draw(self.screen)
        self.blinking_stars.draw(self.screen)
        self.bird.blitme()
        self.monsters.draw(self.screen)

        # Draw the play button if the game is not active
        if not self.game_active:
            self.play_button.draw_button()
            self.exit_button.draw_button()

        pygame.display.flip()  # Update the display to show the changes

if __name__ == '__main__':
    # Make a game instance and run the game
    b_game = BirdGame()
    b_game.run_game()

