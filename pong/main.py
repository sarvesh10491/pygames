import pygame
import pong as p

def gameloop():
    run = True

    while run:
        pong.clock.tick(pong.FPS)
        pong.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        pong.move_paddle(keys)

        pong.move_ball()

    pygame.quit()

if __name__ == '__main__':
    pong = p.Pong()
    gameloop()
