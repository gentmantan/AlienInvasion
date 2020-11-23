import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        # self.settings == ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get is rectangle.
        self.image = pygame.image.load('/home/brigantine/sandbox/'
                        + 'learningpython/AlienInvasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False
        
        self.x = float(self.rect.x)

    def update(self):
        # Update ship x value instead of rect
        if self.moving_right:
            self.rect.x += self.settings.ship_speed
        elif self.moving_left:
            self.rect.x -= self.settings.ship_speed

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
        
