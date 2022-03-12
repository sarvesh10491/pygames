import pygame
from res.colors import *
from res.fonts import *

pygame.init()

class Pong:
    def __init__(self, w=700, h=500):
        # Screen
        self.WIDTH = w
        self.HEIGHT = h

        # Game objects
        self.PADDLE_WIDTH = 20
        self.PADDLE_HEIGHT = 100
        self.BALL_RADIUS = 7

        self.L_score = 0
        self.R_score = 0
        self.WINNING_SCORE = 1

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

        # Init ball
        self.ball = Ball(self.WIDTH//2, self.HEIGHT//2, self.BALL_RADIUS)


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

        # Draw paddles
        self.L_pad.draw(self.display)
        self.R_pad.draw(self.display)

        # Draw ball
        self.ball.draw(self.display)

        # Draw divider
        for i in range(10, self.HEIGHT, self.HEIGHT//20):
            if i % 2 == 1:
                continue
            pygame.draw.rect(self.display, white, (self.WIDTH//2 - 5, i, 10, self.HEIGHT//20))
        
        # Draw scores
        self.L_score_txt = score_font.render(f"{self.L_score}", 1, orange)
        self.R_score_txt = score_font.render(f"{self.R_score}", 1, orange)
        self.display.blit(self.L_score_txt, (self.WIDTH//4 - self.L_score_txt.get_width()//2, 20))
        self.display.blit(self.R_score_txt, (self.WIDTH * (3/4) - self.R_score_txt.get_width()//2, 20))

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

    def move_ball(self):
        self.ball.move()

    def bounce_engine(self, cur_paddle="R"):
        # Reverse current x direction.
        self.ball.x_vel *= -1

        # Get vertical offset between ball center & collided paddle center to determine return velocity & direction
        if cur_paddle=="L":
            self.mid_y = self.L_pad.y + self.L_pad.height/2
        else:
            self.mid_y = self.R_pad.y + self.R_pad.height/2
        self.diff_y = self.mid_y - self.ball.y

        # reduction factor = (max possible y offset) / (max possible velocity)
        self.reduction_factor = (self.L_pad.height / 2) / self.ball.MAX_VEL 

        # New y velocity = vertical offset / reduction factor.
        # e.g for collision at corner, vertical offset = max possible y offset. Thus new y velocity = Max possible velocity
        #     for collision at center, vertical offset = 0. Thus change in y velocity = 0
        self.y_vel = self.diff_y / self.reduction_factor

        # Update y direction with new velocity
        self.ball.y_vel = int(-1 * self.y_vel)

    def handle_bounce(self):
        # -ive y_vel => Going up
        # +ive y_vel => Going down
        # -ive x_vel => Going left
        # +ive x_vel => Going right

        # Check for collisions with ceiling & ground. Reverse y movement direction based on that.
        if (self.ball.y + self.ball.radius >= self.HEIGHT) or (self.ball.y - self.ball.radius <= 0):
            self.ball.y_vel *= -1

        if self.ball.x_vel < 0:     # Moving to left. Check for left paddle.
            if self.ball.y >= self.L_pad.y and self.ball.y <= self.L_pad.y + self.L_pad.height: # Check to see if ball is within left paddle's height bounds
                if self.ball.x - self.ball.radius <= self.L_pad.x + self.L_pad.width: # Check to see if ball is touching the right edge of left paddle
                    # Successful collision with left paddle.
                    self.bounce_engine("L")

        else:     # Moving to right. Check for right paddle.
            if self.ball.y >= self.R_pad.y and self.ball.y <= self.R_pad.y + self.R_pad.height: # Check to see if ball is within right paddle's height bounds
                if self.ball.x + self.ball.radius >= self.R_pad.x: # Check to see if ball is touching the left edge of right paddle
                    # Successful collision with right paddle.
                    self.bounce_engine("R")

    def check_play(self):
        if self.ball.x < 0:
            self.R_score += 1
            self.ball.reset()
        elif self.ball.x > self.WIDTH:
            self.L_score += 1
            self.ball.reset()

    def update_postgame(self, isLeftWinner):
        if isLeftWinner: win_text = "Left won"
        else: win_text = "Right won"

        # # Draw final scores
        # self.L_score_txt = score_font.render(f"{self.L_score}", 1, orange)
        # self.R_score_txt = score_font.render(f"{self.R_score}", 1, orange)
        # self.display.blit(self.L_score_txt, (self.WIDTH//4 - self.L_score_txt.get_width()//2, 20))
        # self.display.blit(self.R_score_txt, (self.WIDTH * (3/4) - self.R_score_txt.get_width()//2, 20))

        text = score_font.render(win_text, 1, pink)
        self.display.blit(text, (self.WIDTH//2 - text.get_width() // 2, 
                        self.HEIGHT//2 - text.get_height()//2))
        
        pygame.display.update()
        

    def is_GameOver(self):
        if self.L_score == self.WINNING_SCORE or self.R_score == self.WINNING_SCORE:
            self.update_postgame(self.L_score == self.WINNING_SCORE)
            return True
        else:
            return False


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
        self.COLOR = red
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





