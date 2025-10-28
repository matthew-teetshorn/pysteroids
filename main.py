import pygame

from constants import *
from player import *

# All objects which can be updated
updatable = pygame.sprite.Group()
# All objects which can be drawn
drawable = pygame.sprite.Group()

# Assign relevant groups to the player
Player.containers = (updatable, drawable)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Handle the window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update the updatables
        updatable.update(dt)
        
        # Handle screen buffer
        screen.fill("black")
        # We must iterate over drawable to call overridden .draw() method
        # as our 'hand drawn' player sprite does not have a .image attr
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        # update the clock (60 FPS)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
