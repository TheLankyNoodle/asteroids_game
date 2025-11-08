# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
from asteroidfield import AsteroidField
from asteroid import Asteroid
import pygame
from constants import *
from logger import log_state, log_event
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0
    
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding_with(player):
                log_event("player_hit")
                print("Game over")
                sys.exit()

        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
