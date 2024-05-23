# Example file showing a basic pygame "game loop"
import pygame
import threading
import time
import os


# pygame setup
class Character():
    def __init__(self, width, height, image, ai_refrence, character_name ):
        
        self.width = width
        self.height = height
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
        self.image = image
        self.ai_model = ai_refrence
        self.character_name = character_name

    def start(self):
        
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME, pygame.SCALED)
        # screen.
        pygame.display.set_caption(self.character_name)
        screen.fill('green')
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)
            pygame.display.flip()

if __name__ == "__main__":
    character = Character(512, 780, "image", "ai", "character")
    character.start()

    