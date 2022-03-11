import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
smallfont = pygame.font.SysFont("comicsansms", 25)



class Pong:
    def __init__(self, w=700, h=500):
        self.WIDTH = w
        self.HEIGHT = h

        self.PADDLE_WIDTH, self.PADDLE_HEIGHT = 20, 100
        self.BALL_RADIUS = 7
        self.WINNING_SCORE = 10

        # Init paddles
        self.L_pad = Paddle(10,
                            self.HEIGHT//2 - self.PADDLE_HEIGHT//2,
                            self.PADDLE_WIDTH,
                            self.PADDLE_HEIGHT,
                            yellow
                            )
    
        self.R_pad = Paddle(self.WIDTH - 10 - self.PADDLE_WIDTH,
                            self.HEIGHT//2 - self.PADDLE_HEIGHT//2,
                            self.PADDLE_WIDTH,
                            self.PADDLE_HEIGHT,
                            green
                            )


        # Init display
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pong")
        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)

        # Init clock
        self.FPS = 60
        self.clock = pygame.time.Clock()
    
    def draw(self):
        self.display.fill(black)

        self.L_pad.draw(self.display)
        self.R_pad.draw(self.display)

        pygame.display.update()
    
    def move_paddle(self, keys):
        if keys[pygame.K_w] and self.L_pad.y - self.L_pad.VEL >= 0:
            self.L_pad.move(up=True)
        if keys[pygame.K_s] and self.L_pad.y + self.L_pad.VEL + self.PADDLE_HEIGHT <= self.HEIGHT:
            self.L_pad.move(up=False)

        if keys[pygame.K_UP] and self.R_pad.y - self.R_pad.VEL >= 0:
            self.R_pad.move(up=True)
        if keys[pygame.K_DOWN] and self.R_pad.y + self.R_pad.VEL + self.PADDLE_HEIGHT <= self.HEIGHT:
            self.R_pad.move(up=False)


class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.COLOR = color
        self.VEL = 4

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        

class Ball:
    def __init__(self, x, y, radius):
        self.MAX_VEL = 5
        self.COLOR = yellow
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1





