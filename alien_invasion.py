import sys

import pygame

class AlienInvasion:
    """Manage game assets and behavior"""

    def __init__(self):
        """Initalizes game using pygame module"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color(230, 230, 230)
        
    def run_game(self):
        """Main function for the game"""
        while True:
            # Listen to keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Make recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make an instance of the AlienInvasion class, then call the run_game func.
    ai = AlienInvasion()
    ai.run_game()