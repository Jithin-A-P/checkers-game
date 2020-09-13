import pygame
from checkers.constants import *
from checkers.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

        board.draw_cubes(WIN)
        pygame.display.update()
    
    pygame.quit()

main()