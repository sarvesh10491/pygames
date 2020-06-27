#Snake Tutorial Python

import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
maroon = (133, 5, 22)
green = (0,255,0)
darkgreen = (0, 115, 33)
blue = (0,0,255)
yellow = (255,255,0)
chrome = (181, 152, 5)
magenta = (204, 52, 235)
orange = (235, 153, 52)
lime = (245, 255, 214)
purple = (99, 66, 219)
cyan = (157, 250, 244)
grey = ((187, 187, 187))
lavender = (171, 171, 235)
pink = (255, 186, 254)

width = 800
height = 600

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Tanks")
icon = headImg = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 40)
largefont = pygame.font.SysFont("comicsansms", 60)


clock = pygame.time.Clock()
fps = 10


def gameIntro():
    intro = True

    surface.fill(black)
    msg_to_screen("*** Welcome to Tanks ***",cyan,-100,"large")
    msg_to_screen("Shoot them before getting shoot you..",white,-30,"small")
    # msg_to_screen("Press \"S\" for start.  \"P\" for pause.  \"Q\" for quit", yellow, 10, "small")

    while intro:
        button("Play", 200,450,100,80, "play", darkgreen, green)
        button("Controls", 350,450,100,80, "controls", chrome, yellow)
        button("Quit", 500,450,100,80, "quit", maroon, red)

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


def gameControls():
    gcont = True

    surface.fill(black)
        
    msg_to_screen("--- Controls ---",grey,-100,"large")
    msg_to_screen("Fire : Spacebar", orange,-30,"small")
    msg_to_screen("Move Tank : Up & Down keys", orange,10,"small")
    msg_to_screen("Move Turret : Left & Right keys", orange,50,"small")
    # button("Back", 350,450,100,80, "backtointro", cyan, lavender)
    

    while gcont:
        button("Back", 20,500,100,80, "backtointro", cyan, lavender)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        


def button(text, x, y, wd, ht, action=None, inactColor=grey, actColor=white, textColor=black):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < cur[0] < x+wd and y < cur[1] < y+ht:
        pygame.draw.rect(surface, actColor, (x, y, wd, ht))
        if click[0] == 1 and action != None:
            if action == "play":
                gameLoop()
            if action == "controls":
                gameControls()
            if action == "quit":
                pygame.quit()
                quit()
            if action == "backtointro":
                gameIntro()

    else:
        pygame.draw.rect(surface, inactColor, (x, y, wd, ht))
    
    text_to_button(text, textColor, x, y, wd, ht)

def text_to_button(msg, color, buttonX, buttonY, buttonWidth, buttonHeight, size="small"):
    textSurf, textRect = text_object(msg,color,size)
    textRect.center = ((buttonX+(buttonWidth//2)), (buttonY+(buttonHeight//2)))
    surface.blit(textSurf, textRect)


def score(score):
    text = smallfont.render("Score : "+str(score), True, magenta)
    surface.blit(text, [0,0])


def text_object(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def pause():
    paused = True
    # surface.fill(white)
    msg_to_screen("Paused", orange, -100,"large")
    msg_to_screen("Press \"R\" for resume.   \"Q\" for quit", orange, 10, "small")
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
        # clock.tick(5)


def msg_to_screen(msg, color, y_offset=0, size="small"):
    textSurf, textRect = text_object(msg,color,size)
    textRect.center = (width//2),(height//2)+y_offset
    surface.blit(textSurf, textRect)


def gameLoop():
    gameExit = False
    gameOver = False

    while not gameExit:
        if gameOver:
            surface.fill(lime)
            score(snakeLen-1)
            msg_to_screen("Game over!", blue, -30, "large")
            msg_to_screen("Press \"R\" for restart.   \"Q\" for quit", purple, 50, "medium")
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
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_p:
                    pause()

        surface.fill(black)
        pygame.display.update()

        clock.tick(fps)

    msg_to_screen("Game exit", cyan, size="large")
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    

gameIntro()
gameLoop()