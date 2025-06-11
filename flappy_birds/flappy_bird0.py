import pygame

pygame.init()

WIDTH, HEIGHT = 400, 600
BIRD_SIZE = 20
GRAVITY = 0.25
JUMP_STRENGHT = -5

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bird_x = 100
bird_y = HEIGHT // 2
running = True
bird_velocity = 0

clock = pygame.time.Clock()

def render():

    # draw bird
    pygame.draw.rect(screen, GREEN, (bird_x, bird_y, BIRD_SIZE, BIRD_SIZE))

while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = JUMP_STRENGHT

    bird_velocity += GRAVITY
    bird_y += bird_velocity

    if bird_y > HEIGHT or bird_y < 0:
        running = False

    screen.fill((0,0,0))
    render()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()