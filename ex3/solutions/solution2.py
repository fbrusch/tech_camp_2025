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


running = True
while running:

    # this is for closing the app when the user closes the window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(WHITE)

    
    rect = pygame.Rect(x, y, 200, 150)

    pygame.draw.rect(screen, BLUE, rect)

    pygame.display.flip()

    x += vx
    y += vy

    if x > 640:
        vx = -vx

    if x < 0:
        vx = -vx

    if y > 480:
        vy = -vy

    if y < 0:
        vy = -vy
    
    # Gravity

    vy += 0.2


    # wait for a bit (let's aim at 50 fps)
    time.sleep(0.02)


    

# Chiudi Pygame
pygame.quit()
sys.exit()