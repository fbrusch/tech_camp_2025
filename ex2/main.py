import pygame
import sys
import time

# Inizializza Pygame
pygame.init()

# Give a "name" to numbers!
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Give a name to the window
pygame.display.set_caption("Demo Pygame")

# Give names to colors  
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Let's introduce a variable that represents the x coordinate del rettangolo

x = 100

# Loop principale

while True:
 
    # Fill the screen with white

    screen.fill(WHITE)

    # Now the rectangle has a "variable" x!

    pygame.draw.rect(screen, BLUE, (x, 100, 200, 150))

    # Update display
    pygame.display.flip()

    # Move the rectangle a little bit on the right
    x += 5

    # wait for a bit
    time.sleep(1)
    

