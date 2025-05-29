import pygame
import sys

# Inizializza Pygame
pygame.init()

# Imposta dimensioni e crea la finestra
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Demo Pygame")

# Definisci un colore (RGB)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Definisci un rettangolo (x, y, larghezza, altezza)
rect = pygame.Rect(100, 100, 200, 150)

# Loop principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Riempi lo sfondo
    screen.fill(WHITE)

    # Disegna il rettangolo
    pygame.draw.rect(screen, BLUE, rect)

    # Aggiorna il display
    pygame.display.flip()

# Chiudi Pygame
pygame.quit()
sys.exit()