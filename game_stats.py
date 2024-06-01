class GameStats:
   def __init__(self, b_game):
       # Get the game settings
       self.settings = b_game.settings

       # Call the reset_stats method to initialize the game statistics
       self.reset_stats()

   def reset_stats(self):
       # Set the initial number of birds left based on the bird limit from the game settings
       self.birds_left = self.settings.bird_limit
       