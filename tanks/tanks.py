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
fps = 15

tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWidth = 5

groundHeight = 35

introImg = pygame.image.load("intro.jpg")
groundList = ["ground1.png", "ground2.png", "ground3.png", "ground4.png", "ground5.png"]
bgList = ["bg1.jpg", "bg2.jpg", "bg3.jpg", "bg4.jpg", "bg5.jpg", "bg6.jpg", "bg7.jpg", "bg8.jpg"]
wallList = ["wall1.jpg", "wall2.jpg", "wall3.jpg", "wall4.jpg"]



def gameIntro():
    intro = True

    # surface.fill(black)
    surface.blit(introImg,(0,0))

    msg_to_screen("Tanks",cyan,-100,"large")
    # msg_to_screen("*** Welcome to Tanks ***",cyan,-100,"large")
    # msg_to_screen("Shoot them before getting shoot you..",white,-30,"small")

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

    while gcont:
        button("Back", 20,500,100,80, "backtointro", cyan, lavender)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
def gameOverLoop(winner):
    gameover = True

    # surface.fill(black)
    surface.blit(introImg,(0,0))
    msg_to_screen("Game Over",cyan,-100,"large")
    if winner:
        msg_to_screen("You won!!",cyan,-30,"small")
    else:
        msg_to_screen("You Lost!!",cyan,-30,"small")

    while gameover:
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


def msg_to_screen(msg, color, y_offset=0, size="small"):
    textSurf, textRect = text_object(msg,color,size)
    textRect.center = (width//2),(height//2)+y_offset
    surface.blit(textSurf, textRect)


def tank(x,y,turPos):
    x,y = int(x),int(y)

    posTurrets = [(x-27,y-2),(x-26,y-5),(x-25,y-8),(x-23,y-12),(x-20,y-14),(x-18,y-15),(x-15,y-17),
                   (x-13,y-19),(x-11,y-21)]

    pygame.draw.circle(surface, yellow, (x,y), tankHeight//2)
    pygame.draw.rect(surface, yellow, (x-tankHeight,y,tankWidth,tankHeight))
    pygame.draw.line(surface, yellow, (x,y), posTurrets[turPos], turretWidth)

    startX = 15
    for i in range(7):
        pygame.draw.circle(surface, chrome, (x-startX,y+20), wheelWidth)
        startX -= 5
    
    return posTurrets[turPos]


def enemy_tank(x,y,turPos):
    x,y = int(x),int(y)

    posTurrets = [(x+27,y-2),(x+26,y-5),(x+25,y-8),(x+23,y-12),(x+20,y-14),(x+18,y-15),(x+15,y-17),
                   (x+13,y-19),(x+11,y-21)]

    pygame.draw.circle(surface, maroon, (x,y), tankHeight//2)
    pygame.draw.rect(surface, maroon, (x-tankHeight,y,tankWidth,tankHeight))
    pygame.draw.line(surface, maroon, (x,y), posTurrets[turPos], turretWidth)

    startX = 15
    for i in range(7):
        pygame.draw.circle(surface, pink, (x-startX,y+20), wheelWidth)
        startX -= 5
    
    return posTurrets[turPos]


def barrier(wallimg, barX, barHeight, barWidth):
    pygame.draw.rect(surface, lavender, (barX, height-barHeight, barWidth, barHeight))
    # bar_surface = pygame.Surface((barWidth, height-barHeight))
    # bar_surface.blit(wallimg, (barX, height-barHeight))
    # pygame.display.update()


def fireShell(gunPos, tankX, tankY, e_tankX, e_tankY, turPos, firePwr, barX, barWidth, barHeight):
    fire = True
    damage = 0
    startShell = list(gunPos)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(surface, red, (startShell[0],startShell[1]), 5)
        
        startShell[0] -= (12 - turPos)*2

        startShell[1] += int((((startShell[0]-gunPos[0])*0.015/(firePwr/50))**2) - (turPos + turPos/(12-turPos)))
        
        if startShell[1] > height-groundHeight:
            hitX = int((startShell[0]*(height-groundHeight))/startShell[1])
            hitY = height-groundHeight
            explosion(hitX, hitY)
            if e_tankX + 10 > hitX > e_tankX - 10:
                damage = 25
            elif e_tankX + 15 > hitX > e_tankX - 15:
                damage = 18
            elif e_tankX + 25 > hitX > e_tankX - 25:
                damage = 10
            elif e_tankX + 35 > hitX > e_tankX - 35:
                damage = 5
            fire = False

        chk_x1 = startShell[0] <= barX + barWidth
        chk_x2 = startShell[0] >= barX

        chk_y1 = startShell[1] <= height
        chk_y2 = startShell[1] >= height - barHeight

        if chk_x1 and chk_x2 and chk_y1 and chk_y2:
            hitX = startShell[0]
            hitY = startShell[1]
            explosion(hitX, hitY)
            fire = False

        pygame.display.update()
        clock.tick(60)
    
    return damage


def enemy_fireShell(gunPos, tankX, tankY, p_tankX, p_tankY, turPos, firePwr, barX, barWidth, barHeight):
    damage = 0
    curPower = 1
    pwrFound = False

    while not pwrFound:
        curPower += 1
        if curPower > 100:
            pwrFound = True

        fire = True
        startShell = list(gunPos)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # pygame.draw.circle(surface, blue, (startShell[0],startShell[1]), 5)
            
            startShell[0] += (12 - turPos)*2

            startShell[1] += int((((startShell[0]-gunPos[0])*0.015/(curPower/50))**2) - (turPos + turPos/(12-turPos)))
            
            if startShell[1] > height-groundHeight:
                hitX = int((startShell[0]*(height-groundHeight))/startShell[1])
                hitY = height-groundHeight
                # explosion(hitX, hitY)
                if p_tankX+15 >  hitX > p_tankX-15:
                    pwrFound = True
                fire = False

            chk_x1 = startShell[0] <= barX + barWidth
            chk_x2 = startShell[0] >= barX

            chk_y1 = startShell[1] <= height
            chk_y2 = startShell[1] >= height - barHeight

            if chk_x1 and chk_x2 and chk_y1 and chk_y2:
                hitX = startShell[0]
                hitY = startShell[1]
                # explosion(hitX, hitY)
                fire = False

    
    fire = True
    startShell = list(gunPos)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(surface, blue, (startShell[0],startShell[1]), 5)
        
        startShell[0] += (12 - turPos)*2

        curPowerFinal = random.randrange(int(curPower * 0.7), int(curPower * 1.3))
        startShell[1] += int((((startShell[0]-gunPos[0])*0.015/(curPowerFinal/50))**2) - (turPos + turPos/(12-turPos)))
        
        if startShell[1] > height-groundHeight:
            hitX = int((startShell[0]*(height-groundHeight))/startShell[1])
            hitY = height-groundHeight
            explosion(hitX, hitY)
            if p_tankX + 15 > hitX > p_tankX - 15:
                damage = 25
            elif p_tankX + 15 > hitX > p_tankX - 15:
                damage = 18
            elif p_tankX + 25 > hitX > p_tankX - 25:
                damage = 10
            elif p_tankX + 35 > hitX > p_tankX - 35:
                damage = 5

            fire = False

        chk_x1 = startShell[0] <= barX + barWidth
        chk_x2 = startShell[0] >= barX

        chk_y1 = startShell[1] <= height
        chk_y2 = startShell[1] >= height - barHeight

        if chk_x1 and chk_x2 and chk_y1 and chk_y2:
            hitX = startShell[0]
            hitY = startShell[1]
            explosion(hitX, hitY)
            fire = False

        pygame.display.update()
        clock.tick(60)
    
    return damage


def explosion(x, y, size=50):
    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        startExp = x,y
        expColors = [red,orange,yellow,chrome]

        mag = 1

        while mag < size:
            exp_bit_X = x + random.randrange(-1*mag,mag)
            exp_bit_Y = y + random.randrange(-1*mag,mag)

            pygame.draw.circle(surface, expColors[random.randrange(0,4)], (exp_bit_X,exp_bit_Y), random.randrange(0,5))
            mag += 1

            pygame.display.update()
            clock.tick(100)
        
        explode = False


def power(level):
    pygame.draw.rect(surface, grey, ((width//2)-70, 3, 173, 34))
    text = smallfont.render("Power : "+str(level)+" %", True, magenta)
    surface.blit(text, [(width//2)-60,0])


def healthbar(player_health, enemy_health):
    if player_health > 67:
        player_health_color = green
    elif player_health > 33:
        player_health_color = chrome
    else:
        player_health_color = red

    if enemy_health > 67:
        enemy_health_color = green
    elif enemy_health > 33:
        enemy_health_color = chrome
    else:
        enemy_health_color = red

    pygame.draw.rect(surface, player_health_color, (680,25,player_health,25))
    pygame.draw.rect(surface, enemy_health_color, (20,25,enemy_health,25))



def gameLoop():
    gameExit = False
    gameOver = False

    mainTankX = width * 0.9
    mainTankY = height * 0.9
    tankMove = 0
    curTurPos = 0
    chgTur = 0

    enemyTankX = width * 0.1
    enemyTankY = height * 0.9

    barX = (width//2)+random.randint(-0.2*width,0.2*width)
    barHeight = random.randint(0.1*height,0.6*height)
    barWidth = 50

    firePower = 50
    firePwrChg = 0

    player_health = 100
    enemy_health = 100

    bgImg = pygame.image.load(bgList[random.randrange(0, 7)])
    groundImg = pygame.image.load(groundList[random.randrange(0, 4)])
    wallimg = pygame.image.load(wallList[random.randrange(0, 3)])

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
                    tankMove = -5
                elif event.key == pygame.K_RIGHT:
                    tankMove = 5
                elif event.key == pygame.K_UP:
                    chgTur = 1
                elif event.key == pygame.K_DOWN:
                    chgTur = -1
                elif event.key == pygame.K_a:
                    firePwrChg = -1
                elif event.key == pygame.K_s:
                    firePwrChg = 1
                elif event.key == pygame.K_SPACE:
                    edamage = fireShell(gunPos, mainTankX, mainTankY, enemyTankX, enemyTankY, curTurPos, firePower, barX, barWidth, barHeight)
                    pdamage = enemy_fireShell(enemy_gunPos, enemyTankX, enemyTankY, mainTankX, mainTankY, 8, 50, barX, barWidth, barHeight)
                    player_health -= pdamage
                    enemy_health -= edamage

                    eposMove = ['L','R']
                    moveIdx = random.randrange(0,2)
                    for x in range(random.randrange(0,10)):
                        if width * 0.3 > enemyTankX > width * 0.03:
                            if eposMove[moveIdx] == "R":
                                enemyTankX += 5
                            elif eposMove[moveIdx] == "L":
                                enemyTankX -= 5

                            surface.blit(bgImg, (0,0))
                            healthbar(player_health, enemy_health)
                            gunPos = tank(mainTankX, mainTankY, curTurPos)
                            enemy_gunPos = enemy_tank(enemyTankX, enemyTankY, 8)

                            firePower += firePwrChg
                            if firePower > 100: firePower = 100
                            if firePower < 1: firePower = 1
                            power(firePower)

                            barrier(wallimg, barX, barHeight, barWidth)

                            surface.fill(darkgreen, rect=[0, height-groundHeight, width, height])
                            for i in range(4):
                                surface.blit(groundImg, (0+i*200,height-groundHeight))

                            pygame.display.update()
                            clock.tick(fps)



                    if player_health <  1:
                        gameOverLoop(0)
                    elif enemy_health < 1:
                        gameOverLoop(1)

                elif event.key == pygame.K_p:
                    pause()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    chgTur = 0
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_a or event.key == pygame.K_s:
                    firePwrChg = 0

        

        mainTankX += tankMove
        curTurPos += chgTur
        if curTurPos > 8: curTurPos = 8
        elif curTurPos < 0: curTurPos = 0

        if mainTankX - (tankWidth//2) < barX + barWidth:
            mainTankX += 5

        # surface.fill(black)
        surface.blit(bgImg, (0,0))

        healthbar(player_health, enemy_health)

        gunPos = tank(mainTankX, mainTankY, curTurPos)
        enemy_gunPos = enemy_tank(enemyTankX, enemyTankY, 8)

        firePower += firePwrChg
        if firePower > 100: firePower = 100
        if firePower < 1: firePower = 1
        power(firePower)

        barrier(wallimg, barX, barHeight, barWidth)

        surface.fill(darkgreen, rect=[0, height-groundHeight, width, height])
        for i in range(4):
            surface.blit(groundImg, (0+i*200,height-groundHeight))

        pygame.display.update()
        clock.tick(fps)

    pygame.draw.rect(surface, purple, ((width//2)-150, (height//2)-40, 300, 80))
    msg_to_screen("Game exit", cyan, size="large")
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    

gameIntro()
gameLoop()