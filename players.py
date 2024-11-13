import pygame
import colours

class Player(pygame.sprite.Sprite):
    def __init__(self,col,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x + 25,y + 25)

    def get_x(self):
        return self.rect.x
    def get_y(self):
        return self.rect.y
    
class Player1(Player):
    def __init__(self, col, x, y):
        Player.__init__(self,col,x,y)

    def update(self):
        KEY = pygame.key.get_pressed()
        if KEY[pygame.K_a] == True and self.rect.x > 0:
            self.rect.move_ip(-5,0)
        if KEY[pygame.K_d] == True and self.rect.x < 400:
            self.rect.move_ip(5,0)
        if KEY[pygame.K_w] == True and self.rect.y > 0:
            self.rect.move_ip(0,-5)
        if KEY[pygame.K_s] == True and self.rect.y < 550:
            self.rect.move_ip(0,5)
  
class Player2(Player):
    def __init__(self, col, x, y):
        Player.__init__(self,col,x,y)

    def update(self):
        KEY = pygame.key.get_pressed()
        if KEY[pygame.K_LEFT] == True and self.rect.x > 500:
            self.rect.move_ip(-5,0)
        if KEY[pygame.K_RIGHT] == True and self.rect.x < 950:
            self.rect.move_ip(5,0)
        if KEY[pygame.K_UP] == True and self.rect.y > 0:
            self.rect.move_ip(0,-5)
        if KEY[pygame.K_DOWN] == True and self.rect.y < 550:
            self.rect.move_ip(0,5)



PLAYER1 = Player1(colours.GREEN,0,300)
PLAYER2 = Player2(colours.RED,950,300)