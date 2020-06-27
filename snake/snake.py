#Snake Tutorial Python

import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
magenta = (204, 52, 235)
orange = (235, 153, 52)
lime = (245, 255, 214)
purple = (99, 66, 219)
cyan = (157, 250, 244)


width = 800
height = 600
block_size = 20

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Snake")
icon = headImg = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 40)
largefont = pygame.font.SysFont("comicsansms", 60)


clock = pygame.time.Clock()
fps = 10

headImg = pygame.image.load("snakehead.jpg")
bodyImg = pygame.image.load("snakebody.jpg")
foodList = ["food1.jpg","food2.jpg","food3.jpg","food4.jpg","food5.jpg","food6.jpg","food7.jpg"]

direction = "R"


def gameIntro():
    intro = True

    surface.fill(black)
    msg_to_screen("*** Welcome to Snake ***",green,-100,"large")
    msg_to_screen("Nom nom on food..",white,-30,"small")
    msg_to_screen("Press \"S\" for start.  \"P\" for pause.  \"Q\" for quit", yellow, 10, "small")
    pygame.display.update()

    while intro:
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
        # clock.tick(15)


def drawSnake(snakeList,block_size):
    if direction == "R":
        head = pygame.transform.rotate(headImg,0)
    elif direction == "L":
        # head = pygame.transform.rotate(headImg,180)
        head = pygame.transform.flip(headImg,True,False)
    elif direction == "U":
        head = pygame.transform.rotate(headImg,90)
    elif direction == "D":
        head = pygame.transform.rotate(headImg,270)

    surface.blit(head, (snakeList[-1][0],snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        surface.blit(bodyImg, (XnY[0],XnY[1]))
        # pygame.draw.rect(surface,yellow,[XnY[0],XnY[1],block_size,block_size])


def foodGen():
    randFoodX = random.randrange(0, width-block_size, block_size)
    randFoodY = random.randrange(0, height-block_size, block_size)
    return randFoodX, randFoodY


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

    global direction
    direction = "R"

    head_x = width//2
    head_y = height//2

    x_dir_chg = block_size
    y_dir_chg = 0

    snakeList = []
    snakeLen = 1

    foodImg = pygame.image.load(foodList[random.randrange(0, 6)])
    randFoodX, randFoodY = foodGen()

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
                    direction = "L"
                    x_dir_chg = -block_size
                    y_dir_chg = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "R"
                    x_dir_chg = block_size
                    y_dir_chg = 0
                elif event.key == pygame.K_UP:
                    direction = "U"
                    x_dir_chg = 0
                    y_dir_chg = -block_size
                elif event.key == pygame.K_DOWN:
                    direction = "D"
                    x_dir_chg = 0
                    y_dir_chg = block_size
                elif event.key == pygame.K_p:
                    pause()

        head_x += x_dir_chg
        if head_x >= width or head_x < 0 or head_y >= height or head_y < 0:  
            gameOver = True
        head_y += y_dir_chg

        surface.fill(black)

        surface.blit(foodImg, (randFoodX,randFoodY))

        snakeHead = [head_x, head_y]
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLen:
            del snakeList[0]

        for eachSeg in snakeList[:-1]:
            if snakeHead == eachSeg:
                gameOver = True

        drawSnake(snakeList,block_size)
        score(snakeLen-1)
        pygame.display.update()

        if head_x == randFoodX and head_y == randFoodY:
            randFoodX, randFoodY = foodGen()
            snakeLen += 1
            foodImg = pygame.image.load(foodList[random.randrange(0, 7)])

        clock.tick(fps)

    msg_to_screen("Game exit", cyan, size="large")
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    


gameIntro()
gameLoop()