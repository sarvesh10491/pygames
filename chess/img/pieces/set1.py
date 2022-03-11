import pygame
import os.path

filepath = os.path.dirname(__file__)
pygame.init()

BlackRook = pygame.image.load(os.path.join(filepath, "BlackRook.png"))
BlackBishop = pygame.image.load(os.path.join(filepath, "BlackBishop.png"))
BlackKnight = pygame.image.load(os.path.join(filepath, "BlackKnight.png"))
BlackPawn = pygame.image.load(os.path.join(filepath, "BlackPawn.png"))
BlackQueen = pygame.image.load(os.path.join(filepath, "BlackQueen.png"))
BlackKing = pygame.image.load(os.path.join(filepath, "BlackKing.png"))

WhiteRook = pygame.image.load(os.path.join(filepath, "WhiteRook.png"))
WhiteBishop = pygame.image.load(os.path.join(filepath, "WhiteBishop.png"))
WhiteKnight = pygame.image.load(os.path.join(filepath, "WhiteKnight.png"))
WhitePawn = pygame.image.load(os.path.join(filepath, "WhitePawn.png"))
WhiteQueen = pygame.image.load(os.path.join(filepath, "WhiteQueen.png"))
WhiteKing = pygame.image.load(os.path.join(filepath, "WhiteKing.png"))

pieces = {
    'r':BlackRook,
    'n':BlackKnight,
    'b':BlackBishop,
    'k':BlackKing,
    'q':BlackQueen,
    'p':BlackPawn,
    'R':WhiteRook,
    'N':WhiteKnight,
    'B':WhiteBishop,
    'K':WhiteKing,
    'Q':WhiteQueen,
    'P':WhitePawn
}