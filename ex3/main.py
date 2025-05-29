import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Demo Pygame")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


x = 100

# also the speed is a variable now!
vx = 10



while True:

    screen.fill(WHITE)

    # Now the rectangle has a "variable" x!

    pygame.draw.rect(screen, BLUE, (x, 100, 200, 150))
    pygame.display.flip()

    # Move the rectangle a little bit on the right according to vx
    x += vx

    # if we reach the end of the screen, let's bounce!

    if x > 640:
        vx = -vx

    

    # wait for a bit (let's aim at 50 fps)
    time.sleep(0.02)