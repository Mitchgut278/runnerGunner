import pygame, sys
from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=(50,200))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill('crimson')
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 50
    
    def update(self):
        self.rect.x -= 3

player = Player()
enemy = Enemy()

players = pygame.sprite.Group()
enemies = pygame.sprite.Group()

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    players.update()
    enemies.update()   
    players.draw(screen)
    enemies.draw(screen)

    
 
    
    
    # enemy.draw()

    pygame.display.flip()
    
    clock.tick(60)