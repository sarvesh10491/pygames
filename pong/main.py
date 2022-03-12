import pygame
import pong as p

def gameloop():
    gameExit = False
    gameOver = False

    while not gameExit:
        pong.clock.tick(pong.FPS)
        pong.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                break
        
        keys = pygame.key.get_pressed()
        pong.move_paddle(keys)

        pong.move_ball()

        pong.handle_bounce()

        pong.check_play()

        if pong.is_GameOver():
            gameOver = True
        
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
                        pass

    pygame.quit()

if __name__ == '__main__':
    pong = p.Pong()
    gameloop()
