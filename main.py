# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

pygame.init()

def main():
    print("Imported pygame succesfully")
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    #Initate Graphic User Interface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Infinite game loop 
    while True:
        # Event handling first
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the function (and thus the game)
        
        # Drawing second
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
