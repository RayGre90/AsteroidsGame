import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            "white", 
            (int(self.position.x), int(self.position.y)),
            self.radius,
            width=2
        )
    def update(self, dt, keys):
        # Update the position of the asteroid based on its velocity and delta time
        self.position += self.velocity * dt
        # Check for screen boundaries and wrap around if necessary