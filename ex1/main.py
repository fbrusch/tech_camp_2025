import pygame
import sys

# Initialize pygame
pygame.init()

# Create screen/window
screen = pygame.display.set_mode((800, 600))

# Draw a rectangle
pygame.draw.rect(screen, (0,0,255), (100, 100, 200, 150))
pygame.display.flip()

# Do nothing forever!

while True: pass

