import pygame
from constants import *

print("Starting Asteroids!")
print(f"Screen Width: {SCREEN_WIDTH}")
print(f"Screen Height: {SCREEN_HEIGHT}")


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fill = (0, 0, 0)
screen.fill(fill)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
def main():
    if __name__ == "__main__":
        main()