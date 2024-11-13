import pygame
import colours
import bullets as b
from input_data import WIDTH , HEIGHT
from players import PLAYER1 , PLAYER2

pygame.init()


DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60




MIJLOC = pygame.Rect((450,0,50,600))


CLOCK = pygame.time.Clock()
SPEED = 10



BULLETS = pygame.sprite.Group()
PLAYERS = pygame.sprite.Group()

PLAYERS.add(PLAYER1)
PLAYERS.add(PLAYER2)

def main():
    run = True

    while run:

        DISPLAY.fill(colours.BLUE)

        pygame.draw.rect(DISPLAY , colours.BLACK , MIJLOC)
        
        BULLETS.update()
        BULLETS.draw(DISPLAY)
        PLAYERS.update()
        PLAYERS.draw(DISPLAY)
        
        KEY = pygame.key.get_pressed()

        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet1 = b.Bullet1(colours.WHITE,PLAYER1.get_x() + 50,PLAYER1.get_y() + 25)
                    BULLETS.add(bullet1)
                elif event.key == pygame.K_0:
                    bullet2 = b.Bullet2(colours.GREEN,PLAYER2.get_x(),PLAYER2.get_y() + 25)
                    BULLETS.add(bullet2)
            if event.type == pygame.QUIT:
                run = False

                

        pygame.display.update()
        
    pygame.quit()


main()