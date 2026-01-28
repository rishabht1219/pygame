import pygame
from constants import *
from logger import log_state



def main():
    # Initialize pygame
    pygame.init()
    # Create window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Draw
        screen.fill("black")
        # Refresh screen
        pygame.display.flip()


    print("Starting Asteroids")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)



if __name__ == "__main__":
    main()
