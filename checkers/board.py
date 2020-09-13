import pygame
from .constants import *

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = 12
        self.red_kings = 0
        self.white_left = 12
        self.white_kings = 0
    
    def draw_cubes(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row%2, COLS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
