import pygame
import sys
from logger import log_event
from shot import Shot
from constants import *
from logger import log_state
from asteroid import Asteroid
from asteroidfield import AsteroidField



from Player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT




def main():


    
    # Initialize pygame
    pygame.init()
    # Create window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create the clock
    clock = pygame.time.Clock()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    player = Player(
        SCREEN_WIDTH / 2,
        SCREEN_HEIGHT / 2)


    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)


    # Delta time variable (seconds)
    dt = 0
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        # Shot ↔ Asteroid collisions
        # Shot ↔ Asteroid collisions
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        #Draw
        screen.fill("black")
        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000



    print("Starting Asteroids")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)



if __name__ == "__main__":
    main()
