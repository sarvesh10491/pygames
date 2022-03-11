import pygame

from res.colors import *
from img.pieces.set1 import *

class Board():
    def __init__(self, surface, width, height, darkSqCol, lightSqCol):
        self.surface = surface
        self.darkSqCol = darkSqCol
        self.lightSqCol = lightSqCol
        self.pieces = pieces

        self.board = [
            [[50,50,lightSqCol],[150,50,darkSqCol],[250,50,lightSqCol],[350,50,darkSqCol],[450,50,lightSqCol],[550,50,darkSqCol],[650,50,lightSqCol],[750,50,darkSqCol]],
            [[50,150,darkSqCol],[150,150,lightSqCol],[250,150,darkSqCol],[350,150,lightSqCol],[450,150,darkSqCol],[550,150,lightSqCol],[650,150,darkSqCol],[750,150,lightSqCol]],
            [[50,250,lightSqCol],[150,250,darkSqCol],[250,250,lightSqCol],[350,250,darkSqCol],[450,250,lightSqCol],[550,250,darkSqCol],[650,250,lightSqCol],[750,250,darkSqCol]],
            [[50,350,darkSqCol],[150,350,lightSqCol],[250,350,darkSqCol],[350,350,lightSqCol],[450,350,darkSqCol],[550,350,lightSqCol],[650,350,darkSqCol],[750,350,lightSqCol]],
            [[50,450,lightSqCol],[150,450,darkSqCol],[250,450,lightSqCol],[350,450,darkSqCol],[450,450,lightSqCol],[550,450,darkSqCol],[650,450,lightSqCol],[750,450,darkSqCol]],
            [[50,550,darkSqCol],[150,550,lightSqCol],[250,550,darkSqCol],[350,550,lightSqCol],[450,550,darkSqCol],[550,550,lightSqCol],[650,550,darkSqCol],[750,550,lightSqCol]],
            [[50,650,lightSqCol],[150,650,darkSqCol],[250,650,lightSqCol],[350,650,darkSqCol],[450,650,lightSqCol],[550,650,darkSqCol],[650,650,lightSqCol],[750,650,darkSqCol]],
            [[50,750,darkSqCol],[150,750,lightSqCol],[250,750,darkSqCol],[350,750,lightSqCol],[450,750,darkSqCol],[550,750,lightSqCol],[650,750,darkSqCol],[750,750,lightSqCol]]
        ]


    def boardLayout(self):
        for rank in range(8):
            for file in range(8):
                pygame.draw.rect(self.surface, 
                                self.board[rank][file][2], 
                                (self.board[rank][file][0], self.board[rank][file][1], 100, 100)
                                )
    

    def parseFEN(self, curFEN):
        FENdata = curFEN.split(" ")     # e.g. ['rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR', 'w', 'KQkq', '-', '0', '1']
        piecePos = FENdata[0].split("/")    # e.g. ['rnbqkbnr', 'pppppppp', '8', '8', '8', '8', 'PPPPPPPP', 'RNBQKBNR']
        
        for r in range(8):
            curRank = list(piecePos[r])
            for f in range(len(curRank)):
                if not curRank[f].isnumeric():
                    self.surface.blit(pieces[curRank[f]], (self.board[r][f][0], self.board[r][f][1]))
                else:
                    num = int(curRank[f])
                    while num>0:
                        pygame.draw.rect(self.surface, self.board[r][f][2], (self.board[r][f][0], self.board[r][f][1], 100, 100))
                        num -= 1


    def curBoard(self, curFEN = "rrrrrrrr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.boardLayout()
        self.parseFEN(curFEN)