import pygame
from input_data import WIDTH
from players import PLAYER1 , PLAYER2


class Bullet(pygame.sprite.Sprite):
    def __init__(self,col,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,10))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

class Bullet1(Bullet):
    def __init__(self, col, x, y):
        Bullet.__init__(self,col,x,y)

    def update(self):
        self.rect.move_ip(5,0) 
        if self.rect.right > WIDTH:
            self.kill()
        global PLAYER2
        if PLAYER2.rect.colliderect(self.rect):
            pygame.quit()

class Bullet2(Bullet):
    def __init__(self,col,x,y):
        Bullet.__init__(self,col,x,y)

    def update(self):
        self.rect.move_ip(-5,0) 
        if self.rect.left < 0:
            self.kill()
        global PLAYER1
        if PLAYER1.rect.colliderect(self.rect):
            pygame.quit()
