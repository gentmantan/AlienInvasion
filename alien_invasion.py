import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Manage game assets and behavior"""

    def __init__(self):
        """Initalizes game using pygame module"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """Main function for the game"""
        while True:
            # Listen to keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redraw the screen with bg_color
            self.screen.fill(self.settings.bg_color)

            # Make recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make an instance of the AlienInvasion class, then call the run_game func.
    ai = AlienInvasion()
    ai.run_game()