import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player

def main():
    pygame.init()

print("Starting Asteroids!")
print(f"Screen Width: {SCREEN_WIDTH}")
print(f"Screen Height: {SCREEN_HEIGHT}")

# Initialize groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

# Set containers for the Player class
Player.containers = (updatable, drawable)

# Set containers for the CircleShape class
Asteroid.containers = (asteroids, updatable, drawable)

# Set containers for the AsteroidField class
AsteroidField.containers = (updatable,)

# Initialize the AsteroidField
AsteroidField()

# Create the player object
player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
dt = 0  # Initialize dt before usage
clock = pygame.time.Clock()

# Start of the game loop
while True:
    dt = clock.tick(60) / 1000  # Limit to 60 FPS and calculate delta time in seconds
    keys = pygame.key.get_pressed()
    updatable.update(dt, keys)

    screen.fill((0, 0, 0))  # Clear the screen with black
    for sprite in drawable:   
        sprite.draw(screen)  # Draw the player
    pygame.display.flip()  # Update the display

    for asteroid in asteroids:
        if player.collision(asteroid):
            print("Game Over")
            import sys
            sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    if __name__ == "__main__":
        main()