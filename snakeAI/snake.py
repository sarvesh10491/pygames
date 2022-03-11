import pygame
import time
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
smallfont = pygame.font.SysFont("comicsansms", 25)


class Direction(Enum):
    RIGHT = 1
    LEFT  = 2
    UP    = 3
    DOWN  = 4


Point = namedtuple('Point', 'x, y')

BLOCK_SIZE = 20
SPEED = 40


class SnakeGameAI:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h

        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake")
        icon = headImg = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()
        self.reset()


    def reset(self):
        # init game state
        self.direction = Direction.RIGHT
        self.head = Point(self.w/2, self.h/2)

        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0


    def _place_food(self):
        # x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE )*BLOCK_SIZE
        # y = random.randint(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE )*BLOCK_SIZE
        randFoodX = random.randrange(0, self.w-BLOCK_SIZE, BLOCK_SIZE)
        randFoodY = random.randrange(0, self.h-BLOCK_SIZE, BLOCK_SIZE)
        self.food = Point(randFoodX, randFoodY)
        if self.food in self.snake:
            self._place_food()


    def play_step(self, action):
        self.frame_iteration += 1

        # 1. Check quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 2. move
        self._move(action)  # Update the head
        self.snake.insert(0, self.head)

        # 3. check if game over by collision or punish for no activity for long time
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score

        # 4. place new food or just move
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()

        # 5. update UI and clock
        self._update_ui()
        self.clock.tick(SPEED)

        # 6. return reward, game over and score
        return reward, game_over, self.score


    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
            
        # hits boundary
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        # hits itself
        if pt in self.snake[1:]:
            return True

        return False



    def _update_ui(self):
        self.display.fill(black)

        for pt in self.snake:
            pygame.draw.rect(self.display, green, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, yellow, pygame.Rect(pt.x+4, pt.y+4, 12, 12))

        pygame.draw.rect(self.display, red, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        Scoretext = smallfont.render("Score: " + str(self.score), True, white)
        self.display.blit(Scoretext, [0, 0])
        pygame.display.flip()


    def _move(self, action):
        # [Left, Straight, Right] 

        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [0, 1, 0]):   # No change in current direction.
            new_dir = clock_wise[idx] 
        elif np.array_equal(action, [0, 0, 1]):   # Right turn. U->R/R->D/D->L/L->U.
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx]
        else: # np.array_equal(action, [1, 0, 0]) : Left turn. U->L/L->D/D->R/R->U.
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx]

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)


        
