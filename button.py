import sys
import pygame
import pygame.font

class PlayButton:
   def __init__(self, b_game, msg, y_offset=0):
       # Get the game's screen and its rectangle
       self.screen = b_game.screen
       self.screen_rect = self.screen.get_rect()

       # Set the button's dimensions
       self.width, self.height = 150, 50

       # Set the button's color and text color
       self.button_color = (120, 255, 200)
       self.text_color = (0, 0, 0)

       # Create a font object for rendering text
       self.font = pygame.font.SysFont(None, 50)

       # Create a rectangle for the button
       self.rect = pygame.Rect(0, 0, self.width, self.height)

       # Center the button on the screen
       self.rect.center = self.screen_rect.center
       self.rect.center = (self.screen_rect.centerx, self.screen_rect.centery - y_offset)


       # Prepare the message to be rendered on the button
       self._prep_msg(msg)

   def _prep_msg(self, msg):
       # Render the message text with the button color and text color
       self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

       # Get the rectangle of the rendered message image
       self.msg_image_rect = self.msg_image.get_rect()

       # Center the message image on the button
       self.msg_image_rect.center = self.rect.center

   def draw_button(self):
       # Fill the button rectangle with the button color
       self.screen.fill(self.button_color, self.rect)

       # Draw the message image on the button
       self.screen.blit(self.msg_image, self.msg_image_rect)


class ExitButton():
    def __init__(self, b_game, ex_msg, y_offset=0):
        # _Get the game's screen and its rectangle_
        self.screen = b_game.screen
        self.screen_rect = self.screen.get_rect()

        # _Set the button's dimensions_
        self.width, self.height = 150, 50

        # _Set the button's color and text color_
        self.button_color = (120, 255, 200)
        self.text_color = (0, 0, 0)

        # _Create a font object for rendering text_
        self.font = pygame.font.SysFont(None, 50)

        # _Create a rectangle for the button_
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # _Center the button horizontally and position it below the play button_
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.centery + y_offset

        # _Prepare the message to be rendered on the button_
        self._prep_ex_msg(ex_msg)

    def _prep_ex_msg(self, ex_msg):
        # _Render the message text with the button color and text color_
        self.ex_msg_image = self.font.render(ex_msg, True, self.text_color, self.button_color)

        # _Get the rectangle of the rendered message image_
        self.ex_msg_image_rect = self.ex_msg_image.get_rect()

        # _Center the message image on the button_
        self.ex_msg_image_rect.center = self.rect.center

    def draw_button(self):
        # _Fill the button rectangle with the button color_
        self.screen.fill(self.button_color, self.rect)

        # _Draw the message image on the button_
        self.screen.blit(self.ex_msg_image, self.ex_msg_image_rect)
    
    def check_click(self, mouse_pos):
        # Check if the mouse click position overlaps with the button's rectangle
        if self.rect.collidepoint(mouse_pos):
            # If clicked, exit the game
            pygame.quit()
            sys.exit()


