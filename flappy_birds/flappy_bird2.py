import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
BIRD_SIZE = 20
GRAVITY = 0.25
JUMP_STRENGHT = -5
PIPE_WIDTH = 40
HORIZONTAL_SPEED = 1
PIPE_GAP = 3 * BIRD_SIZE

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREY = (100, 100, 100)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bird_x = 100
bird_y = HEIGHT // 2
running = True
bird_velocity = 0 
pipe_x = WIDTH
pipe_height = HEIGHT // 2

clock = pygame.time.Clock()

def render():

    # draw bird
    pygame.draw.rect(screen, GREEN, (bird_x, bird_y, BIRD_SIZE, BIRD_SIZE))

    # draw higher pipe

    pygame.draw.rect(screen, GREY, (pipe_x, 0, PIPE_WIDTH, pipe_height))


    pygame.draw.rect(screen, GREY, (pipe_x, pipe_height + PIPE_GAP, PIPE_WIDTH, HEIGHT))



while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = JUMP_STRENGHT

    bird_velocity += GRAVITY
    bird_y += bird_velocity

    if bird_y > HEIGHT or bird_y < 0:
        running = False

    pipe_x -= HORIZONTAL_SPEED
    
    if pipe_x + PIPE_WIDTH < 0:
        pipe_x = WIDTH
        pipe_height = random.randint(10, HEIGHT - 2 * BIRD_SIZE)


    screen.fill((0,0,0))
    render()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()