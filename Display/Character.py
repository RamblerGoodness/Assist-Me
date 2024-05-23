# Example file showing a basic pygame "game loop"
import pygame
import win32api
import win32con
import win32gui
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
        pygame.display.set_caption(self.character_name)
        
        #Key out color.
        green = (0, 255, 0)
        
        
        # Create layered window
        hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        
        # Set window transparency color
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*green), 0, win32con.LWA_COLORKEY)
        
        # Set window to key out color
        screen.fill(green)
        
        
        # Start game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(30, 30, 60, 60))
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            clock.tick(60)
            pygame.display.flip()

if __name__ == "__main__":
    character = Character(512, 780, "image", "ai", "character")
    character.start()

    