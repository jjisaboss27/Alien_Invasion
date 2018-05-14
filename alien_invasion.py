import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    # Create screen
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Make ship
    ship = Ship(screen)

    # Main loop of game
    while True:
        # Watch keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw screen
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Draw screen
        pygame.display.flip()


run_game()