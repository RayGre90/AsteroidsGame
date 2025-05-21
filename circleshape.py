import pygame
import sys

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
    
    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            (255, 255, 255),
            self.triangle(),
            2
        )

    def update(self, dt):
        pass