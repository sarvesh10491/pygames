import pygame
import pong as p

def gameloop():
    run = True

    while run:
        pong.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
    pygame.quit()

if __name__ == '__main__':
    pong = p.Pong()
    gameloop()
