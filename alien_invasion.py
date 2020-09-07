import sys
import pygame
 

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230,230,230)
    def run_game(self):
        """Start the main loop of the game"""
        while True:
            """What for mouse and keyboard events"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            """on every change fill the screen with this bg color"""
            self.screen.fill(self.bg_color)
            """Make the most recently drawn screen visible"""
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai =AlienInvasion()
    ai.run_game()
