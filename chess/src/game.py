import pygame

from src.interface import *
from res.colors import *

class Game:
    def __init__(self):
        pygame.init()

        # Screen dimensions
        self.screen_width = 900
        self.screen_height = 900

        self.screen_surface = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.display.set_caption("Chess")

        self.clock = pygame.time.Clock()
        self.fps = 15

        self.interface = Interface(self.screen_surface, self.screen_width, self.screen_height, black, white)


    def gameIntro(self):
        intro = True
        self.screen_surface.fill(lime)

        self.interface.msg_to_screen("Chess", blue, -100, "large")

        while intro:
            if 1 == self.interface.button("1 Player", 200,650,100,80, "one_player", darkgreen, green):
                self.gameLoop(1)
            if 2 == self.interface.button("2 Player", 500,650,100,80, "two_player", chrome, yellow):
                self.gameLoop(2)

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


    def gameLoop(self, num_player):
        print("In gameloop for %d player game"%num_player)
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
                            self.gameLoop(num_player)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
            
            self.interface.drawBoard()
            


        pygame.draw.rect(self.screen_surface, purple, ((self.screen_width//2)-150, (self.screen_height//2)-40, 300, 80))
        self.interface.msg_to_screen("Game exit", cyan, size="large")
        pygame.display.update()
        # pygame.time.sleep(2)
        pygame.quit()