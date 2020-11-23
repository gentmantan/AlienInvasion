import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Manage game assets and behavior"""

    def __init__(self):
        """Initalizes game using pygame module"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)

    def run_game(self):
        """Main function for the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            
    
    def _check_events(self):
        """Responds to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
            

    def _update_screen(self):
        """Updates images on the screen, and flip to the new screen"""
        #Redraw the screen with bg_color
        self.screen.fill(self.settings.bg_color)

        #Draws ship
        self.ship.blitme()

        # Make recently drawn screen visible.
        pygame.display.flip()
        
        print(self.ship.rect)

if __name__ == '__main__':
    # Make an instance of the AlienInvasion class, then call the run_game func.
    ai = AlienInvasion()
    ai.run_game()
