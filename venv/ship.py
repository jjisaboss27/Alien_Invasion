import pygame

class Ship():

    # Initialize the ship and set its starting position.
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # Load ship
        self.image = pygame.image.load('C:/Users/JJBREE01/PycharmProjects/Alien_Invasion/venv/pictures/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    # Update the ship's posistion based on movement flags.
    def update(self):
        # Update ship's center value, not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    # Draw the ship at its current location.
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # Center the ship on the screen.
    def center_ship(self):
        self.center = self.screen_rect.centerx