# Game controls class

import os
import pygame
import sys

sys.path.insert(0, '../res')
from fonts import *
from colors import *

class Game:
    def __init__(self):
        pygame.init()

        # screen dimensions
        self.screen_width = 1200
        self.screen_height = 1200

        self.screen_surface = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.display.set_caption("Chess")

        self.clock = pygame.time.Clock()
        self.fps = 15


    def gameIntro(self):
        intro = True

        self.screen_surface.fill(chrome)

        while intro:
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        intro = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()


    def gameLoop(self):
        gameExit = False
        gameOver = False

        while not gameExit:
            if gameOver:
                self.screen_surface.fill(lime)
                pygame.display.update()

            while gameOver:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameOver = False
                            gameExit = True
                        if event.key == pygame.K_r:
                            self.gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True


        pygame.draw.rect(self.screen_surface, purple, ((self.screen_width//2)-150, (self.screen_height//2)-40, 300, 80))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()