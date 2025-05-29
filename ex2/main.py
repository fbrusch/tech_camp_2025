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



# Loop principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Riempi lo sfondo
    screen.fill(WHITE)

    # Now the rectangle has a "variable" x!

    rect = pygame.Rect(x, 100, 200, 150)

    # Disegna il rettangolo
    pygame.draw.rect(screen, BLUE, rect)

    # Aggiorna il display
    pygame.display.flip()

    # Move the rectangle a little bit on the right
    x += 5

    # wait for a bit
    time.sleep(1)
    

# Chiudi Pygame
pygame.quit()
sys.exit()