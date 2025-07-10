# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *

pygame.init()

def main():
    print("Imported pygame succesfully")
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    #Organizing by group
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    #Initate Graphic User Interface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Clock game
    fps_clock = pygame.time.Clock()
    dt = 0

    # Infinite game loop 
    while True:
        # Event handling first
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the function (and thus the game)
        
        # Drawing second
        screen.fill("black")
        # Hooking rotation
        updatable.update(dt) 
        # Render player
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = fps_clock.tick(60)/1000
       
if __name__ == "__main__":
    main()
