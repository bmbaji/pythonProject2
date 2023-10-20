import pygame
from constants import *

pygame.init()
pygame.display.set_caption("Tic Tac Toe")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
