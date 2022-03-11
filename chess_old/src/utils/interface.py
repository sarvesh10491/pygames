import os
import pygame
import sys

from res.fonts import *
from res.colors import *

pygame.init()

class Interface():
    def __init__(self, surface, width, height):
        self.surface = surface
        self.width = width
        self.height = height


    def msg_to_screen(self, msg, color, y_offset=0, size="small"):
        textSurf, textRect = self.text_object(msg, color, size)
        textRect.center = (self.width//2),(self.height//2)+y_offset
        self.surface.blit(textSurf, textRect)


    def text_object(self, text, color, size):
        if size == "small":
            textSurface = smallfont.render(text, True, color)
        if size == "medium":
            textSurface = medfont.render(text, True, color)
        if size == "large":
            textSurface = largefont.render(text, True, color)
        return textSurface, textSurface.get_rect()


    def button(self, text, x, y, wd, ht, action=None, inactColor=grey, actColor=white, textColor=black):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < cur[0] < x+wd and y < cur[1] < y+ht:
            pygame.draw.rect(self.surface, actColor, (x, y, wd, ht))
            if click[0] == 1 and action != None:
                if action == "one_player":
                    return 1
                if action == "two_player":
                    return 2
        else:
            pygame.draw.rect(self.surface, inactColor, (x, y, wd, ht))
        
        self.text_to_button(text, textColor, x, y, wd, ht)


    def text_to_button(self, msg, color, buttonX, buttonY, buttonWidth, buttonHeight, size="small"):
        textSurf, textRect = self.text_object(msg,color,size)
        textRect.center = ((buttonX+(buttonWidth//2)), (buttonY+(buttonHeight//2)))
        self.surface.blit(textSurf, textRect)