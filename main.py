import pygame
from checkers.constants import *
from checkers.board import Board
from checkers.piece import Piece

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_pos_by_mouseclick(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_pos_by_mouseclick(pygame.mouse.get_pos())
                piece = board.get_piece(row, col)
                #board.move(piece, 4, 3)
        
        board.draw(WIN)
        pygame.display.update()
    
    pygame.quit()

main()