import pygame
import sys
import time

# Inizializza Pygame
pygame.init()

# Imposta dimensioni e crea la finestra
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Demo Pygame")

# Definisci un colore (RGB)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Let's introduce a variable that represents the x coordinate del rettangolo

x = 100
y = 100


# also the speed is a variable now!
vx = 1
vy = 2

e = 0.7
f = 0.01

# Loop principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Riempi lo sfondo
    screen.fill(WHITE)

    # Now the rectangle has a "variable" x!

    rect = pygame.Rect(x, y, 200, 150)

    # Disegna il rettangolo
    pygame.draw.rect(screen, BLUE, rect)

    # Aggiorna il display
    pygame.display.flip()

    # Move the rectangle a little bit on the right
    x += vx
    y += vy

    # if we reach the end of the screen, let's bounce!
    # but with anaelastic collisions!

    if x > 800-200: # the width of our rectangle is 200, so we need to substract it from 640!:
        vx = -vx*e
        x = 800-200

    if x < 0:
        vx = -vx*e
        x = 0

    if y > 600-150: # the height of our rectangle is 150, so we need to substract it from 480!
        vy = -vy*e
        y = 600-150
    
    if y < 0: # the height of our rectangle is 150, so we need to substract it from 480!
        vy = -vy*e
        y = 0
    # Gravity

    vy += 0.2

    # Friction

    vx *= 0.99
    vy *= 0.99



    # wait for a bit (let's aim at 50 fps)
    time.sleep(0.02)


    

# Chiudi Pygame
pygame.quit()
sys.exit()