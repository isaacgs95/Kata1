import pygame

scree_width = 1200
scree_height = 960

#Color
back_color = (200, 200, 200)
light_gray = pygame.Color('grey2')

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((scree_width, scree_height))

while True:
    pygame.display.flip()
    clock.tick(60)

