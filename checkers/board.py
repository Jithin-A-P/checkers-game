import pygame
from .constants import *
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = 12
        self.red_kings = 0
        self.white_left = 12
        self.white_kings = 0
        self.create_pieces()
    
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row%2, COLS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_pieces(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS): 
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED)) 
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def get_piece(self, row, col):
        return self.board[row][col]

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS or row == 0:
            piece.make_king()
            if piece.color == RED:
                self.red_kings += 1
            else:
                self.white_kings += 1


