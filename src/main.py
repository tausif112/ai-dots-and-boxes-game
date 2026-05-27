import pygame

pygame.init()

WIDTH, HEIGHT = 600, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots and Boxes")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((240, 230, 200))
    pygame.display.update()

pygame.quit()